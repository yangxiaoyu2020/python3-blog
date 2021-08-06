FROM mysql:5.7

COPY ./sql  /tmp/sql

RUN mv /tmp/sql/*.sql /docker-entrypoint-initdb.d

RUN rm -rf /tmp/sql


# docker run --name mysql-service -v ~/frank_work/mysql/data:/var/lib/mysql -p 3310:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7c

