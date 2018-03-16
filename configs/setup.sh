#!/bin/bash
dd if=/dev/zero of=/swap bs=1M count=8192
chmod 600 /swap
mkswap /swap
swapon /swap
echo '/swap none swap sw 0 0' >> /etc/fstab

sudo apt-get install mailutils -y
sudo apt-get install postfix -y
cp /root/seo-search-console-api/configs/main.cf /etc/postfix/main.cf
/etc/init.d/postfix restart
cp /root/seo-search-console-api/configs/aliases /etc/
newaliases

wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release -sc)_all.deb
dpkg -i percona-release_0.1-4.$(lsb_release -sc)_all.deb
sudo apt-get update
echo "percona-server-server-5.6 percona-server-server/root_password password root" | debconf-set-selections \
    && echo "percona-server-server-5.6 percona-server-server/root_password_again password flatfy" | debconf-set-selections \
    && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y percona-server-server-5.7 percona-server-client-5.7

sudo apt-get install python-mysqldb -y
sudo apt-get install python-pip -y

sudo pip install --upgrade google-api-python-client
sudo pip install httplib2
sudo pip install oauth2client
sudo pip install mysql-connector-python
pip install pyOpenSSL

wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_5.0.1_amd64.deb
sudo apt-get install -y adduser libfontconfig
sudo dpkg -i grafana_5.0.1_amd64.deb
 sudo /bin/systemctl daemon-reload
 sudo /bin/systemctl enable grafana-server
cp /root/seo-search-console-api/configs/grafana.ini /etc/grafana/
cp /root/seo-search-console-api/configs/grafana.db /var/lib/grafana/
chown grafana:grafana /var/lib/grafana/grafana.db
sudo systemctl enable grafana-server.service
