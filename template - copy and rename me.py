import discord
from discord.ext import commands
import os
import random
import time
import datetime
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
# ^ modules you may want to use ^

TOKEN = 'your_token_here'
GUILD = 'your_guild_here'

bot = commands.Bot(command_prefix='prefix', intents=discord.Intents.all())

# -----checks-----

async def command_check(ctx):
    return True

# -----events-----

# Called when the client has successfully connected to Discord
@bot.event
async def on_connect():
    print(f'{bot.user.name}: Established connection with Discord')

# Called called when the client has disconnected from Discord
@bot.event
async def on_disconnect():
    print(f'{bot.user.name}: Successfully disconnected from Discord')

# Called when the client is done preparing the data received from Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name}: Bot ready')

# Called when someone begins typing a message
@bot.event
async def on_typing(channel, user, when):
    pass

# Called when a Message is created and sent
@bot.event
async def on_message(message):
    print(f'User: {message.author} sent message in channel: {message.channel} at: {message.created_at}')

# -----public commands-----

@bot.command(name='command_name', usage='command_syntax', help='command_description')
async def command_name(ctx, arg1: str, arg2: str, arg3: str):
    pass

# -----private commands-----

@bot.command(name='private_command_name', usage='command_syntax', help='links the bot to a different guild')
@commands.check(command_check)
async def private_command_name(ctx, arg1: str, arg2: str, arg3: str):
    pass

# -----empty functions-----
def empty_function_1(parameters):
    pass

def empty_function_2(parameters):
    pass

def empty_function_3(parameters):
    pass

# runs the client/bot
bot.run(TOKEN)
