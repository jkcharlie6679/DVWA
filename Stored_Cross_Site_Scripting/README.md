# DVWA - Stored Cross Site Scripting Solution

## Introduction
> The stored XSS is like the message board when the user load the message which was in the web. It can do some vulnerability code.

## Low level
> In the low level we can see the source code. It doesn't filter any input. So, we can input some vulnerability code to attack.
> 
> ![](https://i.imgur.com/YZ2FhLL.png)

> Input the follownig text into the message box, then we can attack successfully.
```
<script>alert(/xss/)</script>
```
![](https://i.imgur.com/LABAdN8.png)
> When we refresh the page, it will bump out again.

## Medium level
> In this level it fileter the text which like HTML, CSS or JavsScrpt.
> And message use the module to check the text.
> So, we can write double time on name box to bypass.

> ![](https://i.imgur.com/RPMTaA4.png)

> However, the name has limit to input, we need to use burp Suite to edit our request package.
> Input the following text on txtName.
```
<sc<script>ript>alert(/xss/)</script>
```
> ![](https://i.imgur.com/ohydXCl.png)

> Or we can use the capital letter to bypass.
```
<sc<script>ript>alert(/xss/)</script>
```
![](https://i.imgur.com/bzaWy3h.png)

> Then we can inject the vulnerability code to the message board.

## High level 
> In this level it filter the `<script>` but we still can use the `<img` to attack.
> 
> ![](https://i.imgur.com/Kz7zKTR.png)

> Input the following test on txtName to attack.
```
<img src=1 onerror=alert(/xss/) >
```
![](https://i.imgur.com/KZ2UwTq.png)

> Then message can't load the picture it will bump the error message.
> 
> ![](https://i.imgur.com/4lT4b9t.png)

## Impossible level 
> In the impossibel level it filter the text which like the HTML, CSS or JavaScript.
> So we can't not let it to run some attack code.
> 
> ![](https://i.imgur.com/GGletM2.png)



