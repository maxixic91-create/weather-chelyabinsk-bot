services:
  - type: web
    name: chelyabinsk-weather-bot
    runtime: python
    repo: https://github.com/YOUR_USERNAME/weather-chelvabinsk-bot
    branch: main
    buildCommand: pip install -r requirements.txt
    startCommand: python bot.py
    envVars:
      - key: BOT_TOKEN
        sync: false
        description: Telegram bot token from @BotFather
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: LOG_LEVEL
        value: INFO
    autoDeploy: true
    healthCheckPath: /health
    plan: free
    envVars:
      - key: PORT
        value: 8080
