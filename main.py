import asyncio
import logging
import os
from pathlib import Path

from telethon import TelegramClient


SESSION_DIR = Path(__file__).parent / "sessions"

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


async def main():
    # Get APP ID and Hash from the environment
    telegram_app_id = os.environ.get("TELEGRAM_APP_ID")
    telegram_app_hash = os.environ.get("TELEGRAM_APP_HASH")

    if not (telegram_app_id and telegram_app_hash):
        logger.error(
            "Please set TELEGRAM_APP_ID and TELEGRAM_APP_HASH environment variables."
        )
        exit(1)

    telegram_app_id = int(telegram_app_id)

    phone_number = input("Enter phone number: ").strip()
    session_filename = f"{phone_number.lstrip('+')}.session"
    full_session_path = SESSION_DIR / session_filename
    logger.info(
        f"Session will be created under the following path: {full_session_path}"
    )
    # Remove session if already exists
    full_session_path.unlink(missing_ok=True)
    # Generate a new session
    client = TelegramClient(str(full_session_path), telegram_app_id, telegram_app_hash)
    logger.info(f"Authenticating with phone number: {phone_number}")
    await client.start(phone=phone_number)

    logger.info(f"Session created successfully: {full_session_path!r}")
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
