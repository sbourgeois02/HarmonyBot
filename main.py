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

client=commands.Bot(command_prefix = '$', intents=intents)


#connect to the database through mysqlConnect.py
#dbConn.main()



def init_load():
    for guild in client.guilds:
        if guild.name == GUILD:

          print(
            f'{client.user} is connected to the following guild:\n'
          f'{guild.name}\n'
          )

    members = '\n - '.join([f"{member.name} ({member.status})" for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_ready():
   
    print(f'{client.user} has connected to Discord!')
   
    init_load()
    

client.run(TOKEN)




