from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from helper.database import uploadlimit, usertype, addpre

async def upgrade_user(bot, update, usertype_text, upload_limit):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    uploadlimit(int(user_id), upload_limit)
    usertype(int(user_id), usertype_text)
    addpre(int(user_id))
    await update.message.edit(f"Added successfully To Premium. Upload limit: {upload_limit}")
    await bot.send_message(user_id, f"Hey, you are Upgraded To {usertype_text}. Check your plan here /myplan")
    await bot.send_message(log_channel, f"⚡️ Plan Upgraded successfully 💥\n\nHey, you are Upgraded To {usertype_text}. Check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot, update):
    await upgrade_user(bot, update, "🥉 **Bʀᴏɴᴢᴇ**", 10)

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot, update):
    await upgrade_user(bot, update, "🥈 **Sɪʟᴠᴇʀ **", 50)

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot, update):
    await upgrade_user(bot, update, "🥇 ** Gᴏʟᴅ**", 100)
