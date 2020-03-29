import random
import time
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import threading

Client = discord.Client()
client = commands.Bot(command_prefix="~")

channels_to_clear=[693635584115343420,693635658085957643,693635858598854747,693683702215213106]
@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.upper().startswith('~CLEARCHAT'):
        userID = message.author.id
        ch=message.channel.id
        if(message.channel.id in channels_to_clear):
            chnl=client.get_channel(message.channel.id)
            deleted = await chnl.purge(limit=10000)
            await chnl.send("<@%s> cleared the chat!" % (userID))
        else:
            chnl = client.get_channel(message.channel.id)
            await chnl.send("You may not clear this chat")




if __name__ == "__main__":
    client.run("NjkzNjc0MTU2ODkzNTM2Mjk2.XoAqWA.W4dSbYsMgwjtCgbbqo2yrhtWCU0")

