FROM nginx

COPY html /data/www/html
COPY nginx.conf /etc/nginx/nginx.conf


