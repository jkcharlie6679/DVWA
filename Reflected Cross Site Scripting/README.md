# DVWA - Reflected Cross Site Scripting Solution

## Low level

In this level we can see the source code. It doen't filter anything and put the input the the html.
So, we can use XSS to attack.

![](https://i.imgur.com/VAWEct0.png)

Then we input the following command to the input box.

```javascript
<script>alert(/XSS/)</script>
```

![](https://i.imgur.com/A3hrmYT.png)

Then we can see the alert message.

## Medium level

In this level it will replace the `<script>` to `"`. So, we can write it double time to bypass.
Input the following text to attack.

```javascript
<scr<script>ipt>alert(/XSS/)</script>
```

![](https://i.imgur.com/p5ceMms.png)

Then we can see the alert message.

## High level

In this level we can see the source code, it filter the input and check the double write. So, we can't use the same way to attack.

![](https://i.imgur.com/gurv8K6.png)
We can use the `<img` to attack.
Input the following command to attack.

```html
<img src=1 onerror=alert(/xss/)>
```

![](https://i.imgur.com/Xu6CCap.png)

Then we can see the error message when the image can't load.

## Impossible level

In the impossibel level it filter the text which like the HTML, CSS or JavaScript.
So we can't not let it to run some attack code.

![](https://i.imgur.com/CMOdV1c.png)
