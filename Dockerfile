FROM nginx

COPY html /data/www/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./ssl/ /etc/nginx/ssl/
RUN ls /etc/nginx/ssl/
