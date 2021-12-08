"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from helpers.bot_utils import BOT_NAME, USERNAME
from config import SUPPORT_GROUP, UPDATES_CHANNEL
from translations import START_TEXT, HELP_TEXT, ABOUT_TEXT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Client.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("🜏 ᴛᴜᴛᴏʀɪᴀʟ 🜏", callback_data="help"),
            ],
            [
                InlineKeyboardButton("🜏 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("ɢʀᴏᴜᴘ 🜏", url=f"https://t.me/xxxsquad18plus"),
            ],
            [
                InlineKeyboardButton("🜏 ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("ᴄʟᴏsᴇ 🜏", callback_data="close"),
            ],
            [
               InlineKeyboardButton("➕ 𝐀𝐃𝐃 𝐒𝐈𝐍𝐍𝐄𝐑 𝐓𝐎 𝐆𝐑𝐎𝐔𝐏 ➕", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply_text(f"**{BOT_NAME} ɪs ᴀʟɪᴠᴇ !** 🍻")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("sᴜᴘᴘᴏʀᴛ 🍻", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("sᴜᴘᴘᴏʀᴛ 🍻", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("🜏 ᴛᴜᴛᴏʀɪᴀʟ 🜏", callback_data="help"),
            ],
            [
                InlineKeyboardButton("🜏 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("ɢʀᴏᴜᴘ 🜏", url=f"https://t.me/xxxsquad18plus"),
            ],
            [
                InlineKeyboardButton("🜏 ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("ᴄʟᴏsᴇ 🜏", callback_data="close"),
            ],
            [
               InlineKeyboardButton("➕ 𝐀𝐃𝐃 𝐒𝐈𝐍𝐍𝐄𝐑 𝐓𝐎 𝐆𝐑𝐎𝐔𝐏 ➕", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

