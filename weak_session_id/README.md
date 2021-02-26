# DVWA - Weak Session IDs Solution


## Low level
> In this level we ca use the brup suite to check the response package, and we can found the web just check the `last_session_id` in session. If it doesn't exit, it will set it to zero or add one.
> 
> ![](https://i.imgur.com/PCNaPBu.png)

> So this way is very easy to forgery.

## Medium level
> In medium level wealso use the brup suite to check the response package.
> 
> ![](https://i.imgur.com/edMgT4K.png)

> And compare two package we can know it use the timestamp to be the session_id.
> It is also the easy to frogery.

## High level 
> In high level we can check the session_id in cookie it is the text which use the md5 to encode.
> 
> ![](https://i.imgur.com/mlKKZwh.png)

> And we use the MD5 decryption web to decode the session_id.
> 
> ![](https://i.imgur.com/0YKcs2O.png)
> We get the session_id is 14, it just add one base on the last_session_id and use the MD5 to encode.
> So, it also a easy to forgery.

## Impossible level
> In the impossible level, we can see the source code.
> 
> ![](https://i.imgur.com/DV89cTB.png)

> It use the random number, timestamp and 'Impossible' to do the sha1 to encode.
> 
> Then we can't to guess the session_id.
> It seems a not bad way to build a session id.
