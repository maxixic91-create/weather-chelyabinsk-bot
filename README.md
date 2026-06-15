version: '3.8'

services:
  weather-bot:
    build: .
    container_name: chelyabinsk-weather-bot
    restart: unless-stopped
    env_file:
      - .env
    environment:
      - TZ=Asia/Yekaterinburg
      - PYTHONUNBUFFERED=1
    ports:
      - "8080:8080"
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
