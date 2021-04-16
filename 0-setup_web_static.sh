#!/usr/bin/env bash
#Prepare your web servers
sudo apt-get update
sudo apt-get -y install nginx
if [ ! -d /data/web_static/releases/ ];
then
	sudo mkdir -p /data/web_static/releases/test/;
fi
if [ ! -d /data/web_static/shared/ ];
then
	sudo mkdir -p /data/web_static/shared/;
fi
sudo echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
if [ -L /data/web_static/current ];
then
	sudo rm /data/web_static/current;
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current;
fi
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '53i \\tlocation \/hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
