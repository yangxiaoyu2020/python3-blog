# nginx 配置文件
## nginx.conf 和 default.conf

- deploy service
```shell

docker run --link=p_blog1:p1 --link=p_blog2:p2 --link=p_blog3:p3 -v /Users/francisyang/frank_work/python3-blog/conf/nginx/nginx.conf:/etc/nginx/nginx.conf -v /Users/francisyang/frank_work/python3-blog/conf/nginx/conf.d:/etc/nginx/conf.d -p 8001:8080 -d --name=my_ngnix_blog   nginx

```