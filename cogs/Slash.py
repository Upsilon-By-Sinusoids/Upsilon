import discord 
from discord.ext import commands, tasks
from discord_slash import cog_ext, SlashCommand, SlashContext
from itertools import cycle
import time
import youtube_dl
from async_timeout import timeout
import discord.utils
import math
import asyncpraw
import random
import asyncio
from decouple import config
import functools
import json
import requests
from chess import *
import os
#import chess.svg
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



class Slash(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    #events
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Slash Commands are working')    
  
    @cog_ext.cog_slash(name="hello", description="Greets you")
    async def hello(self, ctx: SlashContext):
        """Greets you"""
        await ctx.send(f'Hey there.')
        
      
    @cog_ext.cog_slash(name="Quote", description="Generates a random Quote")
    async def _quote(self, ctx: SlashContext):
        """generates a randome quote"""
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(embed = discord.Embed(title=f"{quote}", color=discord.Color.blurple()))
    
    @cog_ext.cog_slash(name="coloured", description="Use this to make your name have 3 colors defined by the roles that you ping.")    
    async def _coloured(self, ctx: SlashContext, role1 : discord.Role, role2 : discord.Role, role3 : discord.Role, user : discord.Member=None, number=10):
        """Use this to make your name have 3 colors defined by the roles that you ping."""
        user = user or ctx.author
        roles = [role1, role2, role3]
        message = await ctx.send("Changing Colors now")
        for i in range(int(number)):
            for j in roles:
                await user.add_roles(j)
                #await ctx.send(message)
                await asyncio.sleep(1)
                await user.remove_roles(j)
                await asyncio.sleep(2)
        
    @cog_ext.cog_slash(name="avatar", description="Get your or any other user's avatar")
    async def _avatar(self, ctx: SlashContext, user : discord.Member = None):
        user = user or ctx.author
        pp = user.avatar_url
        embed=discord.Embed(title=f"{user}'s Avatar", description='', color=0x270de7)
        embed.set_image(url=(pp))
        await ctx.send(embed=embed)
        
    @cog_ext.cog_slash(name="invite", description="Generate an invite link to invite this bot to your server")
    async def _invite(self, ctx: SlashContext):
        """Generate an invite link to invite this bot to your server"""
        ur = 'https://discord.com/api/oauth2/authorize?client_id=784473379183788055&permissions=8&scope=bot%20applications.commands'
        time.sleep(0.2)
        omg = 'Have fun using this bot and contact the owner of the server SINUSOIDS if you face any incovenience.'
        embed = discord.Embed(title="Invite Link", url=ur, color=discord.Color.blurple())
        embed.set_footer(text=omg)
        await ctx.send(embed=embed)
        m = f"{ctx.message.author.name} generated an invite link in {ctx.message.guild}"
        channel = self.client.get_channel(845245176888688660)
        await channel.send(m)
        
        
    @cog_ext.cog_slash(name="upvote", description="Vote for me !!!")
    async def _upvote(self, ctx: SlashContext):
        """Vote for me !!!"""
        embed = discord.Embed(title="Vote for Upsilon",url="https://discordbotlist.com/bots/upsilon/upvote",color=discord.Color.green())
        embed.add_field(name="Vote on top.gg !",value="https://top.gg/bot/784473379183788055")
        embed.add_field(name="Vote on Discord Bot List!",value="https://discordbotlist.com/bots/upsilon/upvote")
        embed.set_image(url=("https://cdn.discordapp.com/attachments/784494481159618560/849999269628346398/ucandoit.gif"))
        embed.set_footer(text="Help us grow!")
        await ctx.send(embed=embed)
        
    @cog_ext.cog_slash(name="physics", description="Creates an embed with a link for the Physics Blog -- deltapsifi")
    async def _physics(self, ctx: SlashContext):
        """creates an embed with a link for the science blog -- deltapsifi"""
        embed=discord.Embed(title="A science blog", url="https://deltapsifi.com/", description="A place to learn about various concepts in the fields of Quantum Mechanics, Particle Physics, and Math.", color=0x3c08f7)
        embed.set_author(name="??????", url="https://deltapsifi.com/")
        embed.add_field(name="Click on the link above", value="And make sure to follow the blog in order to get updates directly in your inbox", inline=False)
        embed.set_footer(text="Here one can even talk about various theories in the field of science.")
        await ctx.send(embed=embed)
 
      
    @cog_ext.cog_slash(name="cs", description="creates an embed with a link for the Computer Science Blog -- hackolympus")
    async def _cs(self, ctx: SlashContext):
        """creates an embed with a link for the computer science blog -- hackolympus"""
        embed=discord.Embed(title="A computer science blog", url="https://hackolympus.com/", description="A place to learn about various concepts in the fields of cyber security, linux and many more. ", color=0x3c08f7)
        embed.set_author(name="Zeus", url="https://hackolympus.com/")
        embed.add_field(name="Click on the link above", value="And make sure to follow the blog in order to get updates directly in your inbox", inline=False)
        embed.set_footer(text="it also has various CTFs")
        await ctx.send(embed=embed)
        
       
    @cog_ext.cog_slash(name="support", description="Creates an embed with an invite link for the support server of this bot")
    async def _support(self, ctx: SlashContext):
        """creates an embed with an invite link for the support server of this bot"""
        embed=discord.Embed(title="A wonderful server for Science and Computer Science", url="https://discord.gg/aXVWmDxRmF", description="A great place for discussion, collaboration, getting your doubts cleared and learning new things on a variety of topics like quantum mechanics, quantum computing, astrophysics and many more. ", color=0x08f738)
        embed.set_author(name="SINUSOIDS", url="https://discord.gg/aXVWmDxRmF")
        embed.add_field(name="https://discord.gg/aXVWmDxRmF      ", value="Click on the server name to join the server and please share this invite link.", inline=False)
        embed.set_footer(text="This server was created with the idea that knowledge must be accessible to and attainable by all individuals for free.")
        await ctx.send(embed=embed)
  
      
    @cog_ext.cog_slash(name="serverinfo", description="Gives information about the server and the server invite link")
    async def _serverinfo(self, ctx: SlashContext):
        """Generates an invite link to the server the bot is in."""
        embed=discord.Embed(title=f"Server Invite Link:", url=f'{await ctx.channel.create_invite(max_age="300")}', description=f"{await ctx.channel.create_invite(max_age='300')}", color=discord.Color.purple())
        embed.set_author(name=f"{ctx.channel.guild.name}")
        embed.set_image(url=(f"{ctx.channel.guild.icon_url}"))
        embed.add_field(name="Server Description:", value=f"{ctx.channel.guild.description}", inline=True)
        embed.add_field(name=f"Owner:", value=f"{ctx.channel.guild.owner}", inline=True)
        embed.add_field(name=f"Member Count:", value=f"{ctx.channel.guild.member_count}", inline=True)
        embed.add_field(name=f"Created At:", value=f"{ctx.channel.guild.created_at}", inline=True)
        await ctx.send(embed=embed)
        
       
    @cog_ext.cog_slash(name="clear", description="Deletes messages (Moderators Only)")
    async def clear(self, ctx, amount=10):
        """This commands can be used for bulk message deletion, the default value is 10; however, you can delete as many as you want"""
        if not ctx.author.guild_permissions.manage_messages:
            await ctx.send(f"Take a chill pill, don't do stuff you aren't supposed to.")
            return
        m = f"{amount} messages deleted in {ctx.guild} by {ctx.author}"
        await ctx.channel.purge(limit=int(amount))
        message = await ctx.send(f"{amount} messages deleted")
        await asyncio.sleep(0.6)
        await ctx.delete(message)
        channel = self.client.get_channel(845245176888688660)
        await channel.send(m)
       
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
       
    @cog_ext.cog_slash(name="xkcd", description="Sends an XKCD meme")
    async def _xkcd(self, ctx):
        rand = random.randint(1,2500)
        r = requests.get(f"https://xkcd.com/{rand}/")
        n1 = r.text.find("Image URL")
        u = r.text[n1+48:n1+130]
        x = u.find("png")
        url = u[:x+3]
        title = "An XKCD meme"
        err = discord.Embed(title=f"{title}", description="", color=random.choice(color))
        err.set_image(url=url)

        await ctx.send(embed=err) 
    
            
    
def setup(client):
    client.add_cog(Slash(client))
  
        
      
