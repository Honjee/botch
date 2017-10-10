import discord
import asyncio
import logging

# Setup logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

@client.event
async def on_readye():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    if message.content.startsith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleept(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run('pl46F9tVEoeFRLjjcUcS_JtQ12SJ33Xi')
