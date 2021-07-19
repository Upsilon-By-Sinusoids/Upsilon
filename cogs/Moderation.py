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

ls = [800448021242052659, 808508913447469106, 844128237587791872, 846203896401231882]

def write(a):
    b = open("fileTowrite.txt","w+")
    b.write(a)
    b.close()
    print(a) 
async def record_usage(ctx):
    await ctx.send(f"{ctx.author} used {ctx.command} at {ctx.message.created_at}")

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
        cha = self.client.get_channel(845245176888688660)
        if profanity.contains_profanity(message.content):
            if message.author.id == 784473379183788055:
                return
            if message.guild.id in ls:
                return
            else:
                print(message.content, message.channel, message.guild.name, sep="\t")
                await cha.send(f"``{message.content},  \t   {message.channel},  \t  {message.guild.name}``")
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
            await ctx.send("https://tenor.com/view/hi-hey-chipmunk-gif-9383966")
            await ctx.send(f'Why were u trying to delete a channel 🤨')
            
    #@nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"**WARNING**, __Possible Anarchyst found in Server --> {ctx.author.mention}__")  
        
    
    @commands.has_permissions(manage_roles=True)
    @commands.command(aliases=["takedown","exile"])
    async def arrest(self, ctx, member : discord.Member):
        "Removes all roles of the offender"
        if ctx.author == member: 
            await ctx.send("You can't arrest yourself dummy!")
            return
        l = member.roles
        l.pop(0)
        await member.remove_roles(*l, reason = None, atomic = True)
        embed = discord.Embed(title=f"{member.name}, you are under arrest.",description="""You have the right to remain silent,
anything you say or do can be used against you in the court of law.""", color=discord.Color.red())
        await ctx.send(embed=embed)
        await embed.add_reaction(emoji="✅")
        
        
def setup(client):
    client.add_cog(Moderation(client))
