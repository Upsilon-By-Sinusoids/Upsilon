import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from decouple import config
import json

client = commands.Bot(command_prefix = '.')
status = cycle(['with the Large Hadron Collider', 'with the Hubble Space Telescope', 'with the Astronauts on the International Space Station'])

@client.event
async def on_ready():
    change_status.start()
    print('status changed')

@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print('successfully loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print('successfully unloaded')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!, {round(client.latency * 1000)}ms')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
TOKEN = config('TOKEN')
client.run(TOKEN)
