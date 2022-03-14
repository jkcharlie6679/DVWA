# DVWA - JavaScript Attacks Solution

## Low level

In this level it want us to input the "success".
However, we input the "success" it return the "Invalid token".

![](https://i.imgur.com/FSgl6OB.png)

If we go to check the source code of the page, we can see its token is generate on frontend.

![](https://i.imgur.com/Kv9C6dc.png)

But the value of phrase was set. So we need to use the brup suite to change the token. The token need to use "success" to generate.

![](https://i.imgur.com/cyVfud3.png)

As we can see the token generate use the rot13 and md5 to encode. Therefore, we use the rot13 and md5 to encode by ourself.

![](https://i.imgur.com/b5WfUGn.png)

![](https://i.imgur.com/cXaxzQ2.png)

Then we edit the request package and forward it.
![](https://i.imgur.com/ZHic6vN.png)

We can get the "well done" on page.

![](https://i.imgur.com/tkRZkCe.png)

## Medium level

In this level we can view the source code of the backend, it put the generate_token in the backend.

![](https://i.imgur.com/dEKsvQU.png)

Observe the token we can konw the rule of the token or we can ckeck the source code of backend.
We use the brup suite to edit the request package, then send it.

![](https://i.imgur.com/LKLgntd.png)

We can get the "well done".

![](https://i.imgur.com/fpmMNxR.png)

## High level

We can check the source code of backend.
We can see the js was ecoded.

![](https://i.imgur.com/WEQNIGZ.png)

We can use the [tool](http://deobfuscatejavascript.com/) to decode the code.

![](https://i.imgur.com/xx28AUi.png)

We can see the part of generate_token.

We use the Inspector open the high.js in console.

![](https://i.imgur.com/uLQbUVS.png)

Then run the following command in the console. Then we can get the correct token.

```php
document.getElementById("phrase").value = "success";
token_part_1()
token_part_2("XX")
token_part_3()
```

![](https://i.imgur.com/FHHJkxn.png)

Copy the correct and paste in the brup suite and sent it we can get the "well done".
![](https://i.imgur.com/UZIUaJP.png)

## Impossible level 

You can never trust anything that comes from the user or prevent them from messing with it and so there is no impossible level.

![](https://i.imgur.com/MwsPJKf.png)
