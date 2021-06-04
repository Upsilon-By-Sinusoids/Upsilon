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

ls = ["Corner of the Universe", "Revolutionaries"]

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
            if message.guild.name in ls:
                return
            else:
                print(message.content, message.channel, message.guild.name, sep="\t")
                write((str(message.content) + " " + str(message.channel) + " " +  str(message.guild.name))) 
                await message.channel.send(choice)
                await message.delete()
                
                
    @commands.has_permissions(kick_members=True) 
    @commands.command(hidden=False)
    async def kick(self, ctx, member: discord.Member):
        channel = self.client.get_channel(845245176888688660)
        await member.kick()
        await channel.send(f"{member} was kicked from {ctx.guild} by {ctx.author.name}")
        
        
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def clear(self, ctx, amount=10):
        """This commands can be used for bulk message deletion, the default value is 10; however, you can delete as many as you want"""
        m = f"{amount} messages deleted by {ctx.message.author.name} in {ctx.message.guild}"
        await ctx.channel.purge(limit=amount+1)
        channel = self.client.get_channel(845245176888688660)
        await channel.send(m)
        
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def nuke(self, ctx, channel: discord.TextChannel):
        try:
            m = f"{channel} channel deleted by {ctx.message.author.name} in {ctx.message.guild}"
            await ctx.send(f'A nuke has been dropped on #{channel}')
            chn = self.client.get_channel(845245176888688660)
            await chn.send(m)
            await channel.delete()
        except:
            await ctx.send(f'Why were u trying to delete a channel 🤨')
        
        
        
        
        
        
        
        
        
        
        
        
def setup(client):
    client.add_cog(Moderation(client))
