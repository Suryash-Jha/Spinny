# Box Store

# Screenshots

## Register
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/59630e66-dfbf-46c5-a780-7610e5834f5a)

## Login
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/827d5d80-14bc-4ed9-a060-774047949634)

## Add Box
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/5cc8d5a4-64b3-4989-bf7a-659e1f23cded)

## Update Box
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/946bcd23-4579-44a7-8894-0ed2d090734a)

## Delete Box
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/f25c78e0-7c2f-42a3-b92c-29e0c3c657ae)

## List Boxes 
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/d67b1a00-40fe-4065-afcf-edf1bb2201fb)

## List Boxes with Filters
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/5c0be846-f728-4b8c-ac19-5b702e2aa509)

## List My Boxes
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/c38dd9e2-c783-4119-b6f3-cad42863b2fd)

## Change Configurations (Not Authenticated as of now)
![image](https://github.com/Suryash-Jha/Spinny/assets/84950710/5e8cdab7-84f2-4509-957c-cb1ba9b5db2c)



# Tips for testing Endpoints

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




