# DVWA - File Upload Solution

## Low level
> In this case, we can see the source code, it doesn't filter the file. So, we can upload any file to server. Then we can upload any attacked file.
> 
> ![](https://i.imgur.com/imHuv1M.png)
> Than we can use the URL `http://140.118.121.110:22334/DVWA-master/hackable/uploads/file` to check the file.
> The PHP function `move_uploaded_file()` will limit the size of file need to less than 100kB.
> 
> We also cand use the 'weevely' to generate a php web shell. And upload it.
> Use the command `weevely generate <password>` to generate a php file and upload it.
> Use the URL `http://dvwa.com/dvwa/haclable/uploads/shell.php`, you will get a blank page.
> Use the command `weevely <URL> <password>` to connect and you can use the caoomad to control it.
> 

## Medium level
> In the medium level we can only upload the jpg file. First, we need to rename `shell.php` to `shell.jpg`. Then, we need to use the brup the interrupt the http request and edit the filename in Content - disposition to `shell.php`.
> 
> ![](https://i.imgur.com/ZJfgdUu.png)
> 
> After that we can use the weevely to control the server like low level.
>  

## High levle
> In the medium level we can only upload the jpg file. First, we need to rename `shell.php` to `shell.php.jpg`. 
> And it will check the last part after '.' it need to be jpg or png.
> 
> ![](https://i.imgur.com/lpl3uqT.png)
> 
> After that we can use the weevely to control the server like low level.
> 

## Impossible levle of File Upload
> In this level the web will use 'md5' to rename the file name and add the Anti-CSRF token. After that will the determine the file type, so we can not have way to upload the malicious file.
> 
> ![](https://i.imgur.com/ylvhj2n.png)

## Reference
> https://www.blink.com.tw/board/post/90230/