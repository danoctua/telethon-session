import asyncio
import logging
import os
from pathlib import Path

from telethon import TelegramClient


SESSION_DIR = Path(__file__).parent / "sessions"
DEFAULT_SESSION_NAME = "anon"

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

    session_name = (
        input(f"Enter session name (defaults to {DEFAULT_SESSION_NAME!r}): ").strip()
        or DEFAULT_SESSION_NAME
    )
    session_filename = f"{session_name}.session"
    full_session_path = SESSION_DIR / session_filename
    logger.info(
        f"Session will be created under the following path: {full_session_path}"
    )
    # Remove session if already exists
    full_session_path.unlink(missing_ok=True)
    # Generate a new session
    async with TelegramClient(
        str(full_session_path), telegram_app_id, telegram_app_hash
    ) as client:
        await client.start()

    logger.info(f"Session created successfully: {full_session_path!r}")


if __name__ == "__main__":
    asyncio.run(main())
