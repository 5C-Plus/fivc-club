apt install -y python3-pip && \
apt install -y python3-virtualenv && \
mkdir -p /var/log/fivc-club && \
cd /opt/app/fivc-club && \
virtualenv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
python launchers/manage.py collectstatic && \
apt install -y supervisor && \
apt install -y nginx && \
cp /opt/app/fivc-club/deployments/supervisord.d/fivc-club-web.ini /etc/supervisor/conf.d/fivc-club-web.conf && \
cp /opt/app/fivc-club/deployments/nginx.d/fivc-club.conf /etc/nginx/conf.d/fivc-club.conf && \
rm -fr /usr/share/nginx/html/fivc-club-static && \
rm -fr /usr/share/nginx/html/fivc-club-fe && \
mv /opt/app/fivc-club/launchers/.static /usr/share/nginx/html/fivc-club-static && \
cp -r /opt/app/fivc-club/deployments/pages /usr/share/nginx/html/fivc-club-fe && \
chmod -R 755 /usr/share/nginx/html/fivc-club-static && \
chmod -R 755 /usr/share/nginx/html/fivc-club-fe && \
systemctl enable supervisor.service && \
systemctl enable nginx.service && \
systemctl restart supervisor.service && \
systemctl restart nginx.service
