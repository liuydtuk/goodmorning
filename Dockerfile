FROM python:3.8.16-bullseye
RUN apt-get update && apt-get -y install cron vim systemctl
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
RUN touch /var/log/cron.log
COPY ./utils/ ./utils/
COPY morning.py morning.py
COPY hello.py hello.py
EXPOSE 5000
CMD flask --app hello run && systemctl start cron
