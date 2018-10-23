FROM python:3.7.0-alpine3.8

# RUN apk add --no-cache \
#     uwsgi \
#     uwsgi-python3 \
#     uwsgi-http

RUN apk add --no-cache \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev \
    uwsgi-http && \
    pip install uwsgi

WORKDIR /app
COPY . .
COPY ./release/assets/uwsgi.ini ./uwsgi.ini
RUN pip install -e .
CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
