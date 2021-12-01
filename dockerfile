FROM python:latest
COPY web/index.html web/
COPY server/localhost.pem server/
EXPOSE 4443
CMD python3 webserver-config.py
