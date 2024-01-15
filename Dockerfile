FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /website

# Expensive layers
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

VOLUME /media /static /config
ENV WEBSITE_MEDIA=/media WEBSITE_STATIC=/static

COPY . ./

EXPOSE 8000

RUN ln -s /config ./website/settings

CMD [ "bash", "./docker-entrypoint.sh" ]
