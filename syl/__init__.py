from pyrogram import Client
from config import SESSION, API_ID, API_HASH
# from config import BOT_TOKEN

bot = Client(
      session_name=SESSION,
      api_id=API_ID,
      api_hash=API_HASH,
      plugins=dict(root="{}/plugins".format(__name__))
)

# BOT SETUP

# bot = Client("Syl",
 #            api_id=API_ID,
  #           api_hash=API_HASH,
   #          bot_token=BOT_TOKEN,
      #       plugins=dict(root="{}/plugins".format(__name__)))
