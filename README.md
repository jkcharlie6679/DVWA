# DVWA

## Establish DVWA Environment

### Install the xampp

Use the following command to download the xampp.

```bash
sudo wget https://www.apachefriends.org/xampp-files/8.0.1/xampp-linux-x64-8.0.1-0-installer.run
```

Then use the following command to install the xampp.
`sudo ./xampp-linux-x64-8.0.1-0-installer.run`

After that you can use `sudo /opt/lampp start` to run the xampp.
If want to stop the lampp use `sudo /opt/lampp stop` to stop it.

### Establish the dvwa

Use the following command to download the package.

```bash
sudo wget https://github.com/ethicalhack3r/DVWA/archive/master.zip
```

Uncompressed the package and move it to the `/opt/lampp/htdocs` and rename to `dvwa`.

Use the `http://127.0.0.1/dvwa` you can see the website of dvwa.

Before you "setup/Reset DB" we need to edit the sql part in `./htdocs/dvwa/config/config.inc.php`.

![](https://i.imgur.com/2JwPCXs.png)

Than you can create you DB.

Then you can use the default account to login to website.
|account|password|
|-|-|
|admin|password|

### Turn on the allow_url_include

Use `find /opt -name php.ini` to find the config in the /opt.
And change the "allow_url_include" to `allow_url_include = on`.
Then restart the lampp using `/opt/lampp/lampp restart`.

### reCAPTCHA API key missing

To the [website](https://www.google.com/recaptcha/admin/site/440483970) to registe the function.

Copy the key to the `./DVWA-master/config/config.inc.php`

```php
$_DVWA[ 'recaptcha_public_key' ]  = 'public_key';
$_DVWA[ 'recaptcha_private_key' ] = 'private_key';
```
