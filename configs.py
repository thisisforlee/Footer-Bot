# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 10334626))
    API_HASH = os.environ.get("API_HASH", "b51609b6f0fdbf256b6612fb10e4b266")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5934918890:AAHpMJ_bpiK1iEY9I65GyPVEdeuFBTlJiFI")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Footer-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001979452202))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001979452202)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1799590717))
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://rahulbitbot:rahulbitbot@cluster0.k7xfg.mongodb.net/?retryWrites=true&w=majority")
    START_TEXT = """
Hi, I am Channel Broadcast Footer Bot!

I can add footer to Channel Media Messages. Just add me to the channel as Admin with all rights and setup /settings !!
"""
