import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

Kartik = [
    [
        InlineKeyboardButton(text="ɴᴏᴏʙ", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://graph.org/file/86585b9f3b850353320d4.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀᴡᴀᴋɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ ʙᴀʙʏ ....")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker(
        "CAADBQADcgkAAoCLSFV4lcD251tTkwI"
    )
    await umm.delete()
    await asyncio.sleep(2)
    await m.reply_photo(
        lol,
        caption=f"""ʜᴇᴇʏᴀ, ɪ ᴀᴍ [Wᴀɢᴏɴ⚡](https://t.me/WagonRobot)

       ▱▱▱▱▱▱▱▱▱▱▱▱
➛  ᴍʏ ᴏᴡɴᴇʀ » [𝐊ᴀʀᴛɪᴋ](https://t.me/{WtfAno})
➛  ᴇᴠᴏɴɪᴛʏ  » [▹ᴄʟɪᴄᴋ](https://t.me/Evonity)
➛  ꜱᴜᴘᴘᴏʀᴛ » [▹ᴄʟɪᴄᴋ](https://t.me/EvonixZone)
➛ ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ » 2.0
  ▱▱▱▱▱▱▱▱▱▱▱▱""",
        reply_markup=InlineKeyboardMarkup(Kartik),
    )
__mod_name__ = "Aʟɪᴠᴇ"
__help__ = """
 ©️ [𓆩 𝐊𝗔𝐑𝗧𝐈𝗞 𓆪 #𝙰ƒк 🍁] (f"tg://user?id={AnoxDx}"))

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?"""
