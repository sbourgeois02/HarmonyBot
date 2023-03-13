#main.py
#pip install discord
#pip install dotenv
#pip install mysqlclient

import os

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

import re

import mysqlConnect as dbConn

import pprint

#load the environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#connect to discord
intents=discord.Intents.all()
# intents.members = True
# intents.presences = True
# intents.message_content = True
client = discord.Client(intents=intents)

client=commands.Bot(intents=intents, command_prefix = "$")


def init_load():
    memberList = []
    values = []

    #get guild members
    for guild in client.guilds:
        for member in guild.members:
            memberList.append(member)
            
    #get guild roles
    roleList = []

    
    for role in guild.roles:
          print((role.id, role.name))
          roleList.append((role.id, role.name))

    #get profanitylist
    profanityList = []
          

    dbConn.onLoad(memberList, roleList)


@client.event
async def on_ready():
   
    print(f'{client.user} has connected to Discord!')
    
    init_load()

#Chat Reader
@client.event
async def on_message(message):
    message_content = message.content
    message_author = message.author
   # if dbConn.
   # await message.channel.send('Mind your language, dude!')

@client.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@client.command(name="CreateCommand")
async def CreateCommand(ctx, *args):
    print(*args)
    splitArgs = re.split("\+\+\+", *args)
    print(splitArgs)

    newCommandName = splitArgs[0]
    newCommandPermission = splitArgs[1]
    newCommandScript = splitArgs[2]

    print("New Command\nName: ", newCommandName, "\nPermission Level: ", newCommandPermission,
           "\nScript: ", newCommandScript)
    
    dbConn.storeCommands(newCommandName, newCommandPermission, newCommandScript)

    await ctx.channel.send("Command Created")
client.run(TOKEN)


