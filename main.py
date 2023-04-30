# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")


bot.run(os.environ["DISCORD_TOKEN"])


import time
import requests
import os

print(f"🔄 Gereksinimler Yükleniyor..")
os.system(f"pip install time")
print("❕Bitmek Üzere..") 
os.system(f"pip install requests")
print("❤️ Gereksinimler Yüklendi!\n💖 Geliştirici: @uslanmazmurti")

ID = int()
token = ''
flood = 'Bu Bir Flood Mesajıdır!'

gonderilen = 0

while True:
           requests.post(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={flood}''')
           time.sleep(0.5)
           gonderilen += 1
           print(f"✅ {gonderilen} Kez Gönderildi")
