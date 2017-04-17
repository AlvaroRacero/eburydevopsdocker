FROM python:3.4

ENV group produser
ENV user alvaro

# CREATE USER FOR MICROSERVICE WHO RUNS APP
RUN groupadd -r ${group} 
RUN useradd -r -g ${group} -s /bin/false ${user}

# SET WORKING DIR, INSTALL DEPENDENCIES, SET CONFIG VARIABLES AND PROPAGATE SCRIPT TO CONTAINER

RUN pip install Flask uWSGI requests redis
WORKDIR /app
COPY cmd.sh /cmd.sh
COPY app /app

EXPOSE 5000 9090 9191

CMD ["sh", "/cmd.sh"]