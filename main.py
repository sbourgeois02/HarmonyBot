#main.py
#pip install discord
#pip install dotenv
#pip install mysqlclient

import os

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get

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
    
    userRoles = dbConn.pull_user_roles()

    print(userRoles)

    for guild in client.guilds:
        for member in guild.members:
            if len(member.roles) > 1:
                memRoleID = dbConn.convertRoleID(member.roles[1])
                print(member, member.roles[1].name)
                print(memRoleID)
            else:
                memRoleID = dbConn.convertRoleID(member.roles[0])
                print(member, member.roles[0].name)
                print(memRoleID)

            for user in userRoles:
                if user[0] == member.name and user[1] == member.discriminator and user[2] != memRoleID:
                    print('UPDATE THE ROLE!')

                    if len(member.roles) > 1:
                        role = get(guild.roles, name=member.roles[1].name)
                        await member.remove_roles(role)
                    else:
                        role = get(guild.roles, name=member.roles[0].name)

                    

                    newRoleName = dbConn.reconvertRoleID(user[2])

                    newRole = get(guild.roles, name=newRoleName)

                    await member.add_roles(newRole)




    

    # users = client.get_all_members()
    # for user in users:
    #     print(user.name, "|", user.discriminator)
    #     if user.name == "skrilla" and user.discriminator == 9150:
    #         print("trying to kick")
    #         await kick_user(user)

@client.event
async def on_ready():
   
    print(f'{client.user} has connected to Discord!')
    
    init_load()

#Chat Reader
#@client.event
#async def on_message(message):
    #message_content = message.content
    #message_author = message.author
   # if dbConn.
   # await message.channel.send('Mind your language, dude!')

@client.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@client.command(name="CreateCommand")
async def CreateCommand(ctx, *args):
    print(*args)
    arguments = ' '.join(args)
    splitArgs = re.split("'", arguments, 2)
    print(splitArgs)
    
        

    newCommandName = splitArgs[0]
    
    newCommandScript = splitArgs[1]

    print("New Command\nName: ", newCommandName,
           "\nScript: ", newCommandScript)
    
    dbConn.storeCommands(newCommandName, newCommandScript)

    await ctx.channel.send("Command Created")



@client.command(name="CustomCommand")
async def CustomCommand(ctx, *args):
    print(*args)
    command = str(args[0])
    print(command)
    result = dbConn.customExecute(command)
    print(result)

    object_of_action = ctx.author.mention

    if len(args) > 1:
        object_of_action = str(args[1])
        print(object_of_action)
        

    result = result.replace("%1", object_of_action)

    
    
    # for character in result:
    #     if character == '%' and character+1 == '1':
    #         if len(args) > 1:
    #             result.insert(character, args[2])
    #         if len(args) == 1:
    #              result.insert(character, ctx.message.author)
    
    print(result)
            


    await ctx.channel.send(result)



async def kick_user(user: discord.Member, *, reason = None):
    await user.kick(reason=reason)



client.run(TOKEN)


