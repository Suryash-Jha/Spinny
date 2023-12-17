# Box Store


Use Multipart form, for sending body to the endpoints, as given below
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/6568e61c-f9e7-4fde-b13f-83b597e51485)

Except /register/ & /login/, every other endpoints require an authorization token in 
```
Token <token>
```




## Post Body for /add/ 

```
length, width, height, name

```
## Post Body for /update/id/

```
length, width, height, name

```
## Post Body for /register/ 

```
username, password, type(staff or anything)

```
## Post Body for /login/ 

```
username, password

```

