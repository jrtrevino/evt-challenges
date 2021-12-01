FROM python:latest
COPY web/index.html web/
COPY server/localhost.pem server/
COPY webserver-config.py ./
CMD python3 webserver-config.py 4443 0.0.0.0
