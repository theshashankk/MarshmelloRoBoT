# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤ð¤
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Marshmello"

# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/0d8c72df39fe0cc791e12.jpg"
file2 = "https://telegra.ph/file/36c66d2c56c18ee8170a8.jpg"
file3 = "https://telegra.ph/file/2bf56960923efbb16683a.jpg"
file4 = "https://telegra.ph/file/2c2f8b871049d944b0598.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** Má´ÊsÊá´á´ÊÊá´ Is AÊÉªá´ á´**\n\n"
    pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "â About My System â\n\n"
    pm_caption += f"â¾ **Tá´Êá´á´Êá´É´ Vá´ÊsÉªá´É´** â {version.__version__}\n"
    pm_caption += "â¾ **Sá´á´á´á´Êá´ CÊá´É´É´á´Ê** â [á´á´ÉªÉ´](https://t.me/Marshmellosupport)\n"
    pm_caption += "â¾ **ÊÉªá´á´É´ê±á´**  â [ðð´ð°ð¼ á´á´ÊsÊá´á´ÊÊá´](https://github.com/theshashankk)\n"
    pm_caption += "â¾ **á´á´á´ÊÊÉªÉ¢Êá´ ÊÊ** â [Má´ÊsÊá´á´ÊÊá´](https://github.com/theshashankk/marshmello)\n\n"
    pm_caption += f"â¾ **á´á´á´Éªá´á´** â {uptime}\n\n"
    pm_caption += f"â¾ **á´Ê á´á´sá´á´Ê** â [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    
