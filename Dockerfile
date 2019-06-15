# # this dockerfile is used for product deployments
# FROM python:3.7-alpine
# LABEL maintainer "Akarsh Khatagalli"

# COPY requirements.txt requirements.txt
# RUN apk update && \
#     apk add --virtual build-deps gcc musl-dev && \
#     apk add postgresql-dev && \
#     rm -rf /var/cache/apk/*

# RUN pip install -r requirements.txt

# # delete dependencies required to install certain python packages 
# # so the docker image size is low enough for Zeit now
# RUN apk del build-deps gcc musl-dev

# COPY . /app
# WORKDIR /app

# # for the flask config
# ENV FLASK_ENV=development

# EXPOSE 5000
# ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "manage:app" ]

FROM python:3.6
LABEL maintainer "Akarsh Khatagalli"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="development"
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["run.py"]