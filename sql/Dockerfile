FROM mysql

ENV MYSQL_ROOT_PASSWORD = mysql
ENV MYSQL_DATABASE = opn

EXPOSE 3306

ADD init.sql /docker-entrypoint-init.d
