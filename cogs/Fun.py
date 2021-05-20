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



class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready():
        print("Fun is working")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        lst = ["rock", "paper", "scissors"]
        mlst = ["📄","✂","🥌"]
        if message.content.lower() in lst:
            #await ctx.send(random.choice(mlst))
        
    @commands.command(hidden=True)
    async def rockpaperscissor(self, ctx):
        await ctx.send(f"The game of rock, paper, scissors has started")
        await ctx.send(f"Let's see if you can beat me 🤨")
        rsp = await on_message(response.content)
        
        
    
    
    
    
    
    
    
    
    
    
    
def setup(client):
    client.add_cog(Fun(client))
