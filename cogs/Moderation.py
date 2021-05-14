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

profanity.load_censor_words_from_file("bannedwords.txt")

def write(a):
    b = open("fileTowrite.txt","w+")
    b.write(a)
    b.close()
    print(a) 


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Modertion is working')
        
    
    @commands.Cog.listener()
    async def on_message(self, message):
        responses = [
            "You kiss your mother with that mouth, {}?",\
            "Woah {}, That's some colorful language.",\
            "LANGUAGE! {}",\
            "Hey {}, watch your mouth.",\
            "We don't use that kind of language here, {}."
        ]

        choice = random.choice(responses)
        choice = choice.format(message.author.mention)
        if profanity.contains_profanity(message.content):
            if message.guild.name == "Corner of the Universe":
                return
            else:
                print(message.content, message.channel, message.guild.name, sep="\t")
                write(str(message.content, message.channel, message.guild.name, sep="\t")) 
                await message.channel.send(choice)
                await message.delete()
                
                
    @commands.has_permissions(kick_members=True) 
    @commands.command(hidden=True)
    async def kick(self, ctx, Member: discord.Member):
        await ctx.kick(Member)
        
        
def setup(client):
    client.add_cog(Moderation(client))
