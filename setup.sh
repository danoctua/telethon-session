#!/bin/bash

ENV_FILE=".env"

# Check if .env file doesn't exist
if [ ! -f "$ENV_FILE" ]; then
  echo "No env file found under ${ENV_FILE}, creating one"

  echo "Make sure you have Telegram App credentials ready."
  echo "More information how to obtain these credentials could be found here: https://core.telegram.org/api/obtaining_api_id"

  read -r -p "Click ENTER to continue"

  read -r -p "Enter Telegram App ID: " telegram_app_id
  # Trim whitespace
  telegram_app_id=$(echo "$telegram_app_id" | xargs)

  # Trim whitespace
  read -r -p -s "Enter Telegram App Hash (input will be hidden): " telegram_app_hash
  telegram_app_hash=$(echo "$telegram_app_hash" | xargs)

  echo "TELEGRAM_APP_ID=${telegram_app_id}" > $ENV_FILE
  # Append to the next line
  echo "TELEGRAM_APP_HASH=${telegram_app_hash}" >> $ENV_FILE

  echo "Telegram App credentials are stored in the ${ENV_FILE}."

else
  echo "File ${ENV_FILE} exists. If you want to rewrite it, please remove it manually and try again. Skipping"
fi
