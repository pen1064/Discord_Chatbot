import os
import discord
from discord.ext import tasks
import datetime
from datetime import timedelta
from dotenv import load_dotenv 
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')
target_channel_id = your_channel_id
Forbidden_Word = ['crap', 'shit', 'fuck', 'bitch']
Greetings = ['!hello', 'hello', 'hi', '!hi', 'hey', '!hey']
client = discord.Client()
msg_time = '2022-2-15 13:34'#24hrs
f = '%Y-%m-%d %H:%M'
msg_content = "This is a scheduled message. Meow! @ " + msg_time


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    message_channel = client.get_channel(target_channel_id)
    await message_channel.send("Let's welcome Charlie, the bot")
    schedule_msg1.start()
    #client.loop.create_task(schedule_msg())


@client.event
async def on_message(message):
    flag = []
    if message.author == client.user:
        return
    for g in Greetings:
        if message.content.lower().startswith(g):
            msg = 'Hello {0.author.mention}'.format(message)
            await message.channel.send(msg)
    flag = [b  for b in Forbidden_Word if b in message.content.lower()]
    if len(flag)>0:
        msg = "{0.author.mention} Watch out your language! We're a peaceful community! Relax!".format(message)
        flag = []
        await message.channel.send(msg)


async def background_task():
    await client.wait_until_ready()
    message_channel = client.get_channel(target_channel_id) 
    while not client.is_closed():    
        await message_channel.send("I am a bot")
        await asyncio.sleep(10)

@tasks.loop(seconds=1)
async def schedule_msg1():
    message_channel = client.get_channel(target_channel_id)
    while not client.is_closed():
        await asyncio.sleep(60)
        current_time = datetime.datetime.strftime(datetime.datetime.now(), f)
        diff = (datetime.datetime.strptime(msg_time, f) - datetime.datetime.strptime(current_time, f)).total_seconds()
        if diff == 0:
            await message_channel.send(msg_content)
            await asyncio.sleep(60)


          
client.run(TOKEN)
