from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as tbot
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/63ec234e1be1f16345e69.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**โก I,m Lovely๐** \n\n"
  LOVELY += "**โก I'm Working with awesome speed**\n\n"
  LOVELY += "**โก Lovely : 2.0 LATEST**\n\n"
  LOVELY += "**โก My Creator :** [๐ง๐จ๐ฆ๐๐๐ฅ๐](t.me/Tushar204)\n\n"
  LOVELY += "**โก Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("๐๐๐๐๐๐๐๐", "https://t.me/LOVELYAPPEAL"), Button.url("๐๐๐๐๐๐", "https://t.me/LOVELY_ROBOTS")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
