---
title: From sqlx to db - golang ORMs
author: koblas
layout: post
date: 2018-03-22T18:43:22+00:00
url: /p/from-sqlx-to-db---golang-orms/643
categories:
  - technical
  - golang

---

# Switching from sqlx to db.v3	
Short post -- ended up switching from [sqlx](https://github.com/jmoiron/sqlx) to [db.v3](https://github.com/upper/db) since I felt that the sqlx layer was more likely to be error prone.

### db.v3 example


{{< highlight go>}}
func (u *UserService) UpdateUser(user *model.User, args struct {
	Name     *string
	Email    *string
	Password *string
}) (*model.User, error) {
	update := make(map[string]interface{})

	if args.Password != nil {
		user.HashPassword(*args.Password)
		update["password"] = user.Password
	}
	if args.Name != nil && *args.Name != user.Name {
		update["name"] = *args.Name
	}
	if args.Email != nil && *args.Email != user.Email {
		update["email"] = *args.Email
	}

	if len(update) == 0 {
		return user, nil
	}
	update["updated_at"] = "NOW()"

	err := u.db.Collection("users")
	       .Find(db.Cond{"id": user.ID}).Update(update)

	if err != nil {
		return user, err
	}

	return user, nil
}
{{< / highlight >}}

### sqlx example

{{< highlight go>}}
func (u *UserService) UpdateUser(user *model.User, args struct {
	Name     *string
	Email    *string
	Password *string
}) (*model.User, error) {
   update := []string{}

	if args.Password != nil {
		user.HashPassword(*args.Password)
		update = append(update, "password = :password")
	}
	if args.Name != nil && *args.Name != user.Name {
		update = append(update, "name = :name")
	}
	if args.Email != nil && *args.Email != user.Email {
		update = append(update, "email = :email")
	}

	if len(update) == 0 {
		return user, nil
	}

	_, err := u.db.NamedExec(
	  fmt.Sprintf(`UPDATE users SET %s, updated_at = NOW() WHERE = :id`,
	              strings.Join(",", update)), user);

	if err != nil {
		return user, err
	}

	return user, nil
}
{{< / highlight >}}
