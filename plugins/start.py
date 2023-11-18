import os 
from pyrogram import Client, filters
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    await message.reply_text(f"🤖 Original BOT: <a href='https://t.me/FlashRenamer_bot'>Fʟᴀsʜ Rᴇɴᴀᴍᴇ Bᴏᴛ ⚡️</a>\nCreator: <a href='https://t.me/Praxxsh'>A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ</a>\nLanguage: Python3\nLibrary: Pyrogram 2.0\nServer: KOYEB\nTotal Renamed File: {total_rename}\nTotal Size Renamed: {humanbytes(int(total_size))} ❤️", quote=True)
