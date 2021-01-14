# reference: https://hub.docker.com/_/python/
FROM python:3.8

LABEL maintainer="Vitaly Korystov"

# Set environment variables
# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /app

COPY . /app

# Install python libraries
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5050

CMD ["uwsgi", "--socket", "0.0.0.0:5050", "--protocol=http", "-w", "wsgi:app"]