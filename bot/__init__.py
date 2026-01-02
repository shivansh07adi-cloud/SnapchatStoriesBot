import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID","35493276"))
    API_HASH = os.environ.get("API_HASH","4b6b15c5aa8546bf3b9d5c6f2ddf724d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","8565552947:AAFfruzlvyBqgjtY5OHol7tKM9F1Z1ZvJxk")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","YTtoAudio07Bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
