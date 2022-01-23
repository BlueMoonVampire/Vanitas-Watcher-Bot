from syl import bot
from config import LOGS
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# decode word for help

# "SPAM", "SPAMING", "SPAMMER", "spam", "spaming", "spammer",
# "Spam", "Spammer", "Spaming', "SCAM", "SCAMING", "SCAMMER",
# "Scam", "Scaming", "Scammer", "scam", "scaming", "scammer",
# "BITCOIN", "Bitcoin", "bitcoin", "btc", "Btc", "BTC",
# "MASS ADD", "MASS ADDER", "MASS ADDING", "Mass Adder", "Mass Adding", "Mass Add",
# "mass add", "mass adding", "mass adder", "Who Add", "Who add", "who add",
# "add member", "Add Member", "Add member", "adding member", "Adding Member", "Adding member",
# "raid", "raider", "raiding", "RAID", "RAIDING", "RAIDER",  "Raid", "Raider', "Raiding", "pron", "Pron", "PRON",
# "Hot Girl", "Hot girl", "hot girl", "xnxx", "Xnxx", "XNXX"



@bot.on_message()
def watch(_, m: Message):
    try:
        if "spam" in m.text or "Spam" in m.text and m.from_user.id:
            k = m.forward(-1001516785366)
            bot.send_message(
                -1001516785366, f"""
    #SYLVIORUSWATCHER
    **Chat** : {m.chat.id}
    **Message Link** :  {m.link}
    **Chat Username** : {m.chat.username}
    """)

    except FloodWait as e:
        asyncio.sleep(e.x)
    except Exception as e:
        print(e)

# All Message Forward

# @bot.on_message()
#def watch(_, m: Message):
#    try:
#        if m.text and m.from_user.id:
#            k = m.forward(LOGS)
#            bot.send_message(
#                LOGS, f"""
#    #SYLVIORUSWATCHER
#    **Chat** : {m.chat.id}
#    **Message Link** :  {m.link}
#    **Chat Username** : {m.chat.username}
#    """)

#    except FloodWait as e:
#        asyncio.sleep(e.x)
#    except Exception as e:
#        print(e)
