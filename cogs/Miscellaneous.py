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


kill = ["https://img.cinemablend.com/filter:scale/quill/c/d/2/8/8/a/cd288aec327829a7589fb0d06cf3474c35352782.gif?mw=600", "https://cdn.discordapp.com/attachments/784494481159618560/849313765703024670/ezgif.com-gif-maker.gif"]


class Miscellaneous(commands.Cog):
    
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
        
    
    @commands.command()
    async def download(self, ctx, song):
        try:
            #link of song from song name
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            #c_path = os.path.dirname(os.path.realpath(__file__))
            #system("spotdl " +  search +" --ignore-ffmpeg-version" )
            for file in os.listdir("./"):
                if file.endswith(".mp4"):
                    name = file
                    print(f"Renamed File: {file}\n")
                    os.rename(file, "song.mp4")

                    await ctx.send(file=discord.File(r'song.mp3'))

                    ctx.voice_client.channel.play(discord.FFmpegPCMAudio("song.mp4"))
                    ctx.voice_client.channel.source = discord.PCMVolumeTransformer(ctx.voice_client.channel.source)
                    ctx.voice_client.channel.source.volume = 0.07
               
        except:
            pass
    
    
    
    
    
    
    
    
def setup(client):
    client.add_cog(Miscellaneous(client))
