# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/MdiskLinkSearchBot'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>FREE</a>

🤖Used In: <a href='https://t.me/blackest_harbour'> GROUP </a></b>
"""

    ABOUT_HELP_TEXT = """<b> Bot ko query smj ana chayeye agar result nhi mila toh search in group @blackest_harbour  </b>
"""

    HOME_TEXT = """
<b> We Are Home {} 🥳
 My Alternate @Mdisk_Links_Sender_Bot
 Search Movies Series Shows {} 🔍 
<a>Send Me Any Movie Series Names🤡 </a></b>
"""

    START_MSG = """
<b>Hello! Dear{}☺️,

I'm Mdisk Search Robot🤖</a>

I Can Search Anything 🔍 What Do You Want {}😳

<a> Request Here If Ur Query Not Found 👉 @blackest_harbour </a></b>
"""



