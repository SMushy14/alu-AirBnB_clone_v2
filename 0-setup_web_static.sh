#!/usr/bin/env bash
# Script that sets up my  web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx 
sudo service nginx start
# Creating parent directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
# Creating a fake HTML file with simple content
echo 'Rethics' | sudo tee /data/web_static/releases/test/index.html
#Creating a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Giving ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
# Updating the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i "38i location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
# Restarting Nginx
sudo service nginx restart
