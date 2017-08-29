FROM ubuntu:latest
MAINTAINER Abhishek Pareek

ARG APT_OPTS='-o Acquire::http::proxy=http://acidia:8123'

RUN apt-get update -y ${APT_OPTS} -qq
RUN apt-get install -y ${APT_OPTS} -qq python-pip python-dev build-essential

COPY ./app /app
WORKDIR /app

RUN pip --proxy http://acidia:8123 install -r requirements.txt

ENTRYPOINT ["uwsgi"]
CMD ["--socket", ":8000", "--protocol", "uwsgi", "-w", "wsgi",  "--callable",  "app", "--master"]
