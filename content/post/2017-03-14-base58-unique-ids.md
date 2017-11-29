---
title: Base58 Unique IDs
author: koblas
type: post
date: 2017-03-14T13:11:41+00:00
url: /p/base58-unique-ids/638
categories:
  - development

---

# Unique IDs

TL;DR version - Use UUIDs, but make them save space.

## Generating Unique IDs

Do you key your whole system by database generated IDs that are autoincrementing integers. As you probably know that means that your APIs and endpoints are ready targets for somebody who wants to test lots of differt IDs against them. After all customer ID # 1000 demonstrates there is probably customer # 1001 and 1002. While you can look at systems like [snowflake](https://github.com/sensorbee/snowflake) it's much easier to build something based on [UUID](https://www.ietf.org/rfc/rfc4122.txt).

```
>>> import uuid
>>> uuid.uuid4()
UUID('73b82667-99bf-4564-82bb-9f95a08ca306')
```

That's 128 bits of uniqueness that makes it possible to do lots of interesting things. Now you don't need to generate a unique ID for everything, you still will have DB tables keyed by IDs, but if you ever think it's going to be public, make the primary ID a UUID based token.

## Making them compact

From DB keys, to anything down the road 128 bits encoded into hex bytes is always going to be 32 bytes (with the `-`s removed). Base16 isn't really the most compact way to save things and storing raw 128 bits in the database sucks for many other reasons.

Compacting; you have a few quick and easy choices.

<table>
  <tr>
    <th>Encoding</th>
    <th>Length/Example</th>
    <th></th>
  </tr>
  <tr>
    <td>Raw</td>
    <td>16 bytes
    <br/>not-printable</td>
    <td>This doesn't transmit over the wire well, encode into JSON or really be useful outside of an internal representation.</td>
  </tr>
  <tr>
    <td>Base 16</td>
    <td>32 characters
    <br/><code>73b82667-99bf-4564-82bb-9f95a08ca306</code></td>
    <td>That's 32 characters, good but not very compact.</td>
  </tr>
  <tr>
    <td>Base 64</td>
    <td>24 / 22 characters
    <br/><code>8G0Cbb7GTHOjpstU5+fuhg==</code></td>
    <td>Good representation, but you have URL issues with the default encoding which includes '/' and '+' (usually translated to '-' and '_' to make it safe)</td>
  </tr>
  <tr>
    <td>Base 32</td>
    <td>32 / 26 characters
    <br/><code>6BWQE3N6YZGHHI5GZNKOPZ7OQY======</code></td>
    <td>We've avoided the URL problems. but it's gotten longer.</td>
  </tr>
    <tr>
    <td><a href="https://en.wikipedia.org/wiki/Base58">Base 58</a></td>
    <td>22 characters
    <br/><code>Wgx98Rbi8nQuL9ddn3mTk1</code></td>
    <td>As compact as Base64, avoiding the URL issues and in a unambigious alphabet and error checks.</td>
  </tr>
</table>

What would I choose to generate unique, customer visible IDs... That's pretty easy. Base58 encoding UUIDs, using the Bitcoin alphabet (this is going to be the default for most Base58 encoders).

Your quick python example, that's it Unique Keys in "one" line of code.

```python
def idGen():
   return b58encode((uuid.uuid4()).bytes)
```

