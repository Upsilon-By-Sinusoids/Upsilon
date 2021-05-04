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
            if 784459718465945631 in message.author.roles or "Strong Nuclear Force" in message.author.roles:
                return
            else:
                print(message.content, message.channel, sep="\n")
                await message.channel.send(choice).add_reaction(":hitler_pepe:")
                await message.delete()
                
                
    @commands.has_permissions(kick_members=True) 
    @commands.command()
    async def kick(self, ctx, Member: discord.Member):
        await ctx.kick(Member)
        
        
def setup(client):
    client.add_cog(Moderation(client))
