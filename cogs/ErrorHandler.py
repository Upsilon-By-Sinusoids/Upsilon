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

x = ["WARNING, UNAUTHORISED COMMAND USAGE by {ctx.author.mention}", "**WARNING**, __Possible Anarchyst found in Server --> {ctx.author.mention}__"]


class ErrorHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        r = random.choice(x)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(r)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f"Sorry buddy, This person does not exist. Promise me you will stop taking drugs to prevent hallucinations.")
        else:
            print(error)
        
         
        
        
def setup(client):
    client.add_cog(ErrorHandler(client))
        
