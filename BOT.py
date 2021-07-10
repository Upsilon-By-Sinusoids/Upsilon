import discord
import time
import os
from discord.ext import commands, tasks
from itertools import cycle
from decouple import config
import json
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents().all()

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intents = intents)
status = cycle(['with the Large Hadron Collider', 'Microsoft Sucks!', 'Discord getting Uglier.😕 '])

@client.event
async def on_ready():
    change_status.start()
    print('status changed')

@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.command.has_permissions(administrator=True)
@client.command(aliases=["prefix"])
async def changeprefix(ctx, prefix):
    """Set a custom prefix for your server"""
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    
    await ctx.send(f"Prefix changed to {prefix}")

@changeprefix.error
async def changeprefix_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        return
    else:
        await ctx.send(f"The following error occured \n {error}")
    
#@client.event
async def on_member_join(cxt, ajrkgbmember): #member only remove everything else to make it work
    await member.send(f'Please provide your Date of Birth, we will use it to greet you on your birthday; if you dont wanna.... type "no".')
    await member.send(f'If u decide to provide your date of birth, please follow the following format: DD/MM')
    try:
        if response.content.lower() == "no": 
            await member.send(f'Alright!')
            await member.send(f'Have a good day ahead and Stay Safe!')
        if response.content.lower().replace('/','').isnum() == True:
            a = response.content.lower()
            while True :
                ask()
                a = datetime.datetime.today()
                for i in list:
                    if a.strftime("%Y/%m/%d") == i : 
                        await member.send(f"Happy Birthday {member}, Enjoy your day!") 
                    time.sleep(60*60*24)
    except: print('failed!')
    

@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@commands.has_role("Strong Nuclear Force")
@client.command(hidden=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'successfully loaded {extension}')

@commands.has_role("Strong Nuclear Force")
@client.command(hidden=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'successfully unloaded {extension}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!, {round(client.latency * 1000)}ms')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
TOKEN = config('TOKEN')
client.run(TOKEN)
