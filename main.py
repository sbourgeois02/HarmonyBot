#main.py
#pip install discord
#pip install dotenv

import os

import discord
from dotenv import load_dotenv

import mysqlConnect as dbConn

#load the environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#connect to discord
client = discord.Client(intents=discord.Intents.default())

#connect to the database through mysqlConnect.py
dbConn.main()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    

client.run(TOKEN)




