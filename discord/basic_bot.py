import discord
import random
import asyncio
from discord.ext import commands
from config import DISCORD_TOKEN
from logger import logger_on
import logging

game = discord.Game(name="betches")
client = discord.Client(game=game)
logger_on()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        print(message.channel.__dir__())
        print(message.channel.get_message(message.author.id))
        counter = 0
        tmp = await message.channel.send('Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await message.channel.send('Done sleeping')

client.run(DISCORD_TOKEN)
