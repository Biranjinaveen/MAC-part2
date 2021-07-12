FROM python:alpine3.7
COPY . /
WORKDIR /
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "flask_ping.py" ]