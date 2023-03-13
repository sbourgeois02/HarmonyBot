#main.py
#pip install discord
#pip install dotenv

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import mysqlConnect as dbConn

import pprint

#load the environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#connect to discord
intents=discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)

client=commands.Bot(intents=intents, command_prefix = '$')


def init_load():
    memberList = []
    values = [()]

    for guild in client.guilds:
        for member in guild.members:
            memberList.append(member)
            
    #print(memberList)
    dbConn.onLoad(memberList)



@client.event
async def on_ready():
   
    print(f'{client.user} has connected to Discord!')
   
    init_load()
    

client.run(TOKEN)




