python3-blog
======================

A NEW PYTHON BLOG 

**PERSONAL USED ONLY**

## setup
### database
```shell
docker run --name mysql-service -v ~/{workdir}/mysql/data:/var/lib/mysql -p 3310:3306 -e MYSQL_ROOT_PASSWORD={自定义} -d mysql:5.7c

```
 

### service
```shell
docker build -t test-blog:0.0.2 . 
```
 


## test

## deploy


```shell
docker run -itd -p 9013:9002 test-blog:0.0.2.
```

## jenkins

