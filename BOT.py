import discord
from discord_slash import SlashCommand, SlashContext
import time
import os
from discord.ext import commands, tasks
from itertools import cycle
from decouple import config
from discord_components import *
import json
import discord
import logging
import asyncio 

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        embed=discord.Embed(title="This is the Help Command. Duh.", description="", color=discord.Color.blurple())
        for cog in mapping:
            if cog == None:
                break
            if len(mapping[cog]) == 0:
                continue
            if cog.qualified_name == "Owner" or cog.qualified_name == "Slash":
                continue
            embed.add_field(name=f"{cog.qualified_name}:", value=f"{[command.name for command in mapping[cog]]}",inline=False)
        embed.add_field(name="Vote for me !!!", value=f"https://top.gg/bot/784473379183788055 \nhttps://discordbotlist.com/bots/upsilon/upvote", inline=False)
        embed.add_field(name="Join the support server for any help", value="https://discord.gg/aXVWmDxRmF", inline=False)
        embed.set_footer(text="Type ``.help <command>`` for more information on a command. \nYou can also type ``.help <category>`` for more info on a category. \nCreated by ΔΨφ#4993 (he's the Devil, so don't play with him 😈)")
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed=discord.Embed(title=f"{cog.qualified_name}", color=discord.Color.green())
        for command in cog.get_commands():
            embed.add_field(name=f"{command.name}", value=f"{command.help} \nUsage: {command.signature}", inline=False)
        embed.add_field(name="Vote for me !!!", value=f"https://top.gg/bot/784473379183788055 \nhttps://discordbotlist.com/bots/upsilon/upvote", inline=False)
        embed.add_field(name="Join the support server for any help", value="https://discord.gg/aXVWmDxRmF", inline=False)
        embed.set_footer(text="Created by ΔΨφ#4993 (he's the Devil, so don't play with him 😈)")
        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command):
        embed=discord.Embed(title=f"{command.name}",description=f"{command.help}", color=discord.Color.red())
        if len(command.aliases) != 0:
            embed.set_author(name=f"Aliases : {command.aliases}")
        else: 
            pass
        if type(command.signature) != None:
            embed.add_field(name=f"Usage:", value=f"{command.signature}", inline=True)
        embed.add_field(name="Vote for me !!!", value=f"https://top.gg/bot/784473379183788055 \nhttps://discordbotlist.com/bots/upsilon/upvote", inline=False)
        embed.add_field(name="Join the support server for any help", value="https://discord.gg/aXVWmDxRmF", inline=False)
        embed.set_footer(text="Created by ΔΨφ#4993 (he's the Devil, so don't play with him 😈)")
        await self.get_destination().send(embed=embed)



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents().all()

client = commands.Bot(command_prefix = '.', help_command=CustomHelpCommand(), case_insensitive=True, intents = intents)
slash = SlashCommand(client, sync_commands=True)
status = cycle(['against Authoritarian Governments that spy on their citizens', 'Microsoft Sucks!!', 'Discord getting Uglier.😕 ', 'SAVE THE TREES'])

@client.event
async def on_ready():
    change_status.start()
    DiscordComponents(client)
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

@client.command(aliases=["prefix"])
@commands.has_permissions(administrator=True)
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
        await ctx.send(f"The following error occured: \n {error}")
    
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

guild_ids=[784455316468793406]    
    
@slash.slash(name='ping', description="Get the bot's latency!")
async def _ping(ctx):
    await ctx.send(f'Pong!, {round(client.latency * 1000)} milliseconds')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!, {round(client.latency * 1000)} milliseconds')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
TOKEN = config('TOKEN')
client.run(TOKEN)
