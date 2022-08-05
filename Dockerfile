FROM alpine:latest
COPY src /usr/share/warseyapifrontend/

EXPOSE 8080

WORKDIR /usr/share/warseyapifrontend/

RUN apk add --update python3 py-pip sqlite

RUN pip3 install flask waitress 

ENTRYPOINT python3 server.py