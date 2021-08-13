# nginx 配置文件
## nginx.conf 和 default.conf

- deploy service
```shell
docker run --name=my_nginx1 --link=python_blog1:p1 --link=python_blog2:p2 --link=python_blog3:p3 \ 
  -v conf/nginx/nginx.conf:/etc/nginx/nginx.conf -v conf/nginx/conf.d:/etc/nginx/conf.d -p 8000:80 -d nginx
```
