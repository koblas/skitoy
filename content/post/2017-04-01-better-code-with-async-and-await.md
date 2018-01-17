---
title: Better code with async and await
author: koblas
type: post
date: 2017-04-01T17:59:09+00:00
url: /p/better-code-with-async-and-await/641
categories:
  - draft

---

# TEXT HERE

```
import RedisSession from "redis-sessions";
import settings from "../../config/settings";
import InvalidTokenError from '../../lib/errors/invalidTokenError';

const rs = new RedisSession({ host: settings.redis.host });

const apiUserAuthMiddleWare = (request, response, next) => {
  const sessionToken = request.headers["token"];

  if (typeof sessionToken === "undefined") {
    return next();
  }

  rs.get(
    {
      app: "api-session",
      token: sessionToken,
    },
    (err, session) => {
      if (err || !session || !session.d) {
        response.header("Access-Control-Allow-Origin", "*");
        return response.status(InvalidTokenError.httpCode)
        .json(InvalidTokenError.errorResponse());
      }
      request.session.user = session.d;
      const db = request.session.db;
      const include = {
        model: db.merchant,
        include: {
          model: db.balance,
          attributes: db.balance.generalAttributes(),
          include: db.currency,
        },
      };
      db.user.findOne({ where: { id: session.d.id }, include })
      .then(
        (user) => {
          request.session.merchant = user.merchant;
          request.session.testMode = user.merchant.testMode;
          return next();
        },
      );
    },
  );
};

export default apiUserAuthMiddleWare;
```


```
import RedisSession from "redis-sessions";
import settings from "../../config/settings";
import InvalidTokenError from '../../lib/errors/invalidTokenError';

const rs = new RedisSession({ host: settings.redis.host });

//
// Convert rs.get() from a callback function to something that returns a Promise
//
const getSession = token => new Promise((resolve, reject) => {
  rs.get({ app: "api-session", token }, (err, session) => {
    if (err) {
      reject(err);
    } else {
      resolve(session);
    }
  });
});

//
//  Pull the merchant information out of the x-session-token header and
//  convert into a merchant id
//
export default async function apiUserAuthMiddleWare(request, response, next) {
  const sessionToken = request.headers["token"];

  if (sessionToken === undefined || !sessionToken) {
    next();
    return;
  }

  let session;
  try {
    session = await getSession(sessionToken);
  } catch (err) {
    // fall through
  }

  if (session === undefined || !session || !session.d) {
    response.header("Access-Control-Allow-Origin", "*");
    response.status(InvalidTokenError.httpCode).json(InvalidTokenError.errorResponse());
    return;
  }

  try {
    request.session.user = session.d;

    const db = request.session.db;
    const include = {
      model: db.merchant,
      include: {
        model: db.balance,
        attributes: db.balance.generalAttributes(),
        include: db.currency,
      },
    };

    const user = await db.user.findOne({ where: { id: session.d.id }, include });

    request.session.merchant = user.merchant;
    request.session.testMode = user.merchant ? user.merchant.testMode : false;
  } catch (err) {
    next(err);
    return;
  }

  next();
}
```
