FROM python:3.8-slim as dependencies
WORKDIR /opt/app

# system dependencies
ENV DOCKERIZE_VERSION v0.6.1
RUN apt update && apt install -y libpq-dev make wget gettext \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# python dependencies
COPY requirements ./requirements
RUN python3 -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements/prod.txt && \
    rm -r requirements

FROM dependencies as code
COPY manage.py Makefile scripts/entrypoint.sh ./
COPY content_storage ./content_storage

FROM code as production

EXPOSE 8000
ENTRYPOINT ./entrypoint.sh
CMD make production
