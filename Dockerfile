FROM ubuntu:16.04
MAINTAINER Mike Miller <chop3593@gmail.com>
RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y build-essential wget ca-certificates apt-utils iputils-ping
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 --version
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN apt-get remove -y postgresql*
RUN apt-get update -y && apt-get install -y \
    postgresql-client-9.6 postgresql-contrib-9.6 postgresql-server-dev-9.6
RUN groupadd docker; usermod -a -G docker postgres
RUN /etc/init.d/postgresql start &&\
    runuser -l postgres -c 'psql --command "CREATE USER docker WITH SUPERUSER;"' &&\
    runuser -l postgres -c 'createdb -O docker pyted;'
RUN echo "local   all             all  trust" > /etc/postgresql/9.6/main/pg_hba.conf
RUN echo "host all  all    0.0.0.0/0  trust" >> /etc/postgresql/9.6/main/pg_hba.conf
RUN cat /etc/postgresql/9.6/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf
EXPOSE 5000 5432
COPY . /app
WORKDIR /app
RUN whoami
RUN python3.6 -m pip install --upgrade pip
RUN python3.6 -m pip install -r requirements.txt
ENTRYPOINT ["bash"]
CMD ["docker/docker_bootstrap.sh"]