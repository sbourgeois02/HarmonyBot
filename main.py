#main.py
#pip install discord
#pip install dotenv
#pip install mysqlclient

import os

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv

import re

import sched, time

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

profanityList = dbConn.pullProfanity()
strikesList = dbConn.pullStrikes()

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

    #dbConn.pullProfanity(profanityList)
          

    dbConn.onLoad(memberList)
    update_db.start()

    
@tasks.loop(minutes=2)
async def update_db():
    print("updating...")
    channel = client.get_channel(1084683040518840350)
    await channel.send("updating database")

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
    arguments = str(args)
    splitArgs = re.split("\s", arguments, 2)
    print(splitArgs)
    # splitArgs = []
    # last = 0
    # for i in args:
    #       if args[i] is not "\s":
    #             splitArgs.append(*args[last:i])
    #             continue
    #       else:
    #             last = i
    #             continue
        

    newCommandName = splitArgs[0]
    
    newCommandScript = splitArgs[1]

    print("New Command\nName: ", newCommandName,
           "\nScript: ", newCommandScript)
    
    dbConn.storeCommands(newCommandName, newCommandScript)

    await ctx.channel.send("Command Created")



@client.command(name="CustomCommand")
async def CustomCommand(ctx, *args):
    command = str(*args)
    result = dbConn.customExecute(command)
    print(result)

    object_of_action = ctx.author.mention

    if len(args) > 1:
        object_of_action = args[2]

    

    result.replace('%1', object_of_action)
    
    # for character in result:
    #     if character == '%' and character+1 == '1':
    #         if len(args) > 1:
    #             result.insert(character, args[2])
    #         if len(args) == 1:
    #              result.insert(character, ctx.message.author)
    #         result.


    await ctx.channel.send(result)




client.run(TOKEN)


