---
title: How to handle Settings for Accounts.
author: koblas
type: post
date: 2008-06-26T22:19:13+00:00
url: /p/how-to-handle-settings-for-accounts/166
pvc_views:
  - 1741
categories:
  - Development
tags:
  - sql
  - design

---
I've run into this problem a few times, but I'm putting out a call to see if anybody has some great insight into a good solution. To date, I've come up with three different approaches to handling user settings, but none of which I'm in love with. Other ideas, other comments, other ways?

Working assumptions

  * It's handy to access specific elements outside of the database (e.g. who has XYZ preference set) 
  * Databases appear to be better at storing small data than large (varchar < 255 vs. BLOB of 64k) 
  * There is no right answer 

## Small records only

First encountered this at Excite with Excite Mail, since we were using OpenWave as the backend we could store 255 bytes in one of their database tables, and it became a preferences store. Though of course it was a bit more restrive than the below SQL, it got the job done. With a bit of class wrapping ontop, it really works.

**Pro:** 

  * Only one record type 

**Con:** 

  * End up with a chained dkey (signature_0, signature_1, etc.) 

```
CREATE TABLE IF NOT EXISTS setting (
    account_id      int unsigned NOT NULL,

    dkey            varchar(20) NOT NULL,
    data            tinyblob NOT NULL,
    created_on      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY     (account_id, dkey),
    FOREIGN KEY     (account_id) REFERENCES account(account_id) ON DELETE CASCADE
) ENGINE=InnoDB;
```

## Small and Big records

Ok, so when you don't want to deal with chaining of records you can create a BIG and SMALL store of data.

**Pro:**

  * No chaining of records 
  * Easily delete keys (just delete from both and ignore errors) 

**Con:**

  * Lots of extra model level helpers to determine where data should go 

```
CREATE TABLE IF NOT EXISTS user_data (
    user_id         varchar(16) NOT NULL,

    dkey            varchar(20) NOT NULL,
    dtype           int DEFAULT 0,
    data            tinyblob,

    created_on      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY     (user_id, dtype, dkey),
    INDEX           (user_id, dtype),
    FOREIGN KEY     (user_id) REFERENCES user(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS user_data_big (
    user_id         varchar(16) NOT NULL,

    dkey            varchar(20) NOT NULL,
    dtype           int DEFAULT 0,
    data            blob,

    created_on      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY     (user_id, dtype, dkey),
    INDEX           (user_id, dtype),
    FOREIGN KEY     (user_id) REFERENCES user(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;
```

## Blob of doom

What about the idea that you don't want your SQL store to have a clue, so save settings in one big blob (json, xml encoded, etc.)

**Pro:**

  * All the parsing is at code level, record management is easy (1 per user) 

**Con:**

  * it's a blob, you can't really access it easily outside of your program 

```
CREATE TABLE IF NOT EXISTS user_blob (
    user_id         varchar(16) NOT NULL,

    data            blob,

    created_on      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX           (user_id),
    FOREIGN KEY     (user_id) REFERENCES user(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;
```

Any other ideas? Cool suggestions, the magic solution I've forgotten?
