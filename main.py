import discord
from discord.ext import commands
import logging
# from dotenv import load_dotenv
import os
import random
import webserver

#kalo mau deploy ke Render pake code ini
DISCORD_TOKEN = os.environ['discordkey']


# load_dotenv()
# token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='nyan', intents=intents)

nyan_random_reply = ['O.O"?','apa..','...','ga','apa ish!?','g','ga mau',':p','apa sayang',':/']

@bot.event
async def on_ready():
    print(f'Logged in as,{bot.user.name}')
    print(bot.user.name)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "nyan" in message.content.lower():
        await message.channel.send(random.choice(nyan_random_reply))

    if "nyan link" in message.content.lower():
        await message.channel.send(f'Nih, jangan sembarang invite orang yaa, {message.author.mention} :3 \nhttps://discord.gg/jywWK32Fgr')

    await bot.process_commands(message)

webserver.keep_alive()
# bot.run(token, log_handler=handler, log_level=logging.DEBUG)
bot.run(DISCORD_TOKEN)
