# FROM ubuntu
# WORKDIR /app
# COPY . /app
# RUN apt-get update && apt-get upgrade -y

# # install node js version 10
# RUN apt-get install curl gnupg wget -yq \
#     && curl -sL https://deb.nodesource.com/setup_10.x | bash \
#     && apt-get install nodejs -yq

# #install libreoffice (for soffice)
# RUN yes | apt-get install libreoffice

# #install python 3.7
# RUN apt update
# RUN apt install software-properties-common
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN yes | apt install python3.7
# RUN yes | apt-get install -y python3-pip

# #install postgress
# RUN yes | apt install postgresql postgresql-contrib
# USER postgres

# # Create a PostgreSQL role named ``docker`` with ``docker`` as the password and
# # then create a database `docker` owned by the ``docker`` role.
# # Note: here we use ``&&\`` to run commands one after the other - the ``\``
# #       allows the RUN command to span multiple lines.
# RUN  /etc/init.d/postgresql start &&\
#     psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
#     createdb -O docker docker

# CMD [ "pip3 install -r package.txt", "python3.7 server.py" ]
# EXPOSE 5000

FROM python:3

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# sudo apt-get install docker-ce=18.06.1~ce~3-0~ubuntu
RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
ENTRYPOINT ["python"]
CMD ["app.py"]