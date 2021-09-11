import discord 
from discord_slash import cog_ext, SlashCommand, SlashContext
from discord.ext import commands, tasks
from itertools import cycle
import time
import youtube_dl
from decouple import config
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


kill = ["https://img.cinemablend.com/filter:scale/quill/c/d/2/8/8/a/cd288aec327829a7589fb0d06cf3474c35352782.gif?mw=600", "https://cdn.discordapp.com/attachments/784494481159618560/849313765703024670/ezgif.com-gif-maker.gif"]

clid = config('clid')
clis = config('clis')
pasw = config('pasw')

reddit = asyncpraw.Reddit(client_id=clid,
                    client_secret=clis,
                    username="SpecialistNo7996",
                    password=pasw,
                    user_agent="pegasus")

color = [discord.Color.blurple(),discord.Color.greyple(),discord.Color.orange(),discord.Color.red(),discord.Color.blue(),discord.Color.dark_purple(),discord.Color.dark_magenta(),discord.Color.green(),discord.Color.purple(),discord.Color.teal()]


class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun is working")
        
    @commands.command()
    async def kill(self, ctx, user : discord.Member):
        if user == ctx.author:
            embed=discord.Embed(title=f"{user}, I know it seems tempting to take the easy way out, my advice is that you listen to some good ol' songs by typing .play [song name].", description='', color=0xe74c3c)
            #embed.set_image(url=("https://tenor.com/MTjK.gif"))
            await ctx.send(embed=embed)
            await asyncio.sleep(1.5)
            await ctx.send(embed=discord.Embed(title="Go on then, what are you waiting for?",description="",color=0xe74c3c))
        else:
            url = random.choice(kill)
            embed=discord.Embed(title=f"{user} was killed by {ctx.author}", description='', color=0xe91e63)
            embed.set_image(url=(url))
            await ctx.send(embed=embed)
      
    @cog_ext.cog_slash(name="kill", description="Your personal Death Note!")
    async def _kill(self, ctx, user : discord.Member):
        if user == ctx.author:
            embed=discord.Embed(title=f"{user}, I know it seems tempting to take the easy way out, my advice is that you listen to some good ol' songs by typing .play [song name].", description='', color=0xe74c3c)
            #embed.set_image(url=("https://tenor.com/MTjK.gif"))
            await ctx.send(embed=embed)
            await asyncio.sleep(1.5)
            await ctx.send(embed=discord.Embed(title="Go on then, what are you waiting for?",description="",color=0xe74c3c))
        else:
            url = random.choice(kill)
            embed=discord.Embed(title=f"{user} was killed by {ctx.author}", description='', color=0xe91e63)
            embed.set_image(url=(url))
            await ctx.send(embed=embed)
            
            
           
       
    @commands.command()
    async def meme(self, ctx):
        subreddit = await reddit.subreddit("memes")
        l = []

        async for i in subreddit.hot(limit=80):
            l.append(i)

        rand = random.choice(l)
        tit = rand.title
        ur = rand.url
        e = discord.Embed(title=f"{tit}", description="", color=random.choice(color))
        e.set_image(url=ur)

        await ctx.send(embed=e)

    @cog_ext.cog_slash(name="meme", description="Sends a reddit meme")
    async def meme(self, ctx):
        subreddit = await reddit.subreddit("memes")
        l = []

        async for i in subreddit.hot(limit=80):
            l.append(i)

        rand = random.choice(l)
        tit = rand.title
        ur = rand.url
        e = discord.Embed(title=f"{tit}", description="", color=random.choice(color))
        e.set_image(url=ur)

        await ctx.send(embed=e)
        
    
   
    
    
    
    
    
    
    
def setup(client):
    client.add_cog(Fun(client))
