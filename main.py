# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram import Client

bot_token = os.environ["6484301475:AAHh1svu7-ZzVNgpXQmf8nHQbocLEMlGboI"]
api_id = int(os.environ["29849415"])
api_hash = os.environ["0dd6c10897b85d7f10a8dcdeb74f8b8a"]

plugins = dict(
    root="plugins"
)

Bot = Client(
    "Movie-Info-Bot-V2",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins
)

Bot.run()
