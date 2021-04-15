#!/usr/bin/env bash
# Sets up your web servers for the deployment

apt-get update
apt-get -y install nginx

service nginx start

mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" |sudo tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu: /data/
sed -i '/listen 80 default_server/ a location /hbnb_static {\n alias /data/web_static/current/;\n}\n'  /etc/nginx/sites-available/default
sudo service nginx restart
