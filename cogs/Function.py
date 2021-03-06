import discord 
from discord.ext import commands, tasks
from discord_slash import cog_ext, SlashCommand, SlashContext
from itertools import cycle
import time
import youtube_dl
from async_timeout import timeout
import discord.utils
import math
import random
from discord_components import DiscordComponents, Button, ButtonStyle
from discord_slash.utils.manage_components import wait_for_component
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
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


class Function(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    #events
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
       
    @commands.Cog.listener()
    async def on_message(self, message):
        li = [800448021242052659, 784455316468793406]
        c = message.content
        if message.channel.guild.id not in li:
            return
        if len(message.mentions) >= 7:
            await message.author.ban(reason = "pinging")
        
    #@commands.Cog.listener()
    #async def on_message(message):
    #    if message.content.startswith('owner')
    #        await message.send(f'message.guild.owner_id')
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print('{} joined by bot'.format(guild))
        message = '{} joined by bot and the server id is ``{}``'.format(guild, guild.id)
        channel = self.client.get_channel(845245176888688660)    
        await channel.send(message)
        for i in guild.channels:
            x = await i.create_invite(self, max_age='300')
        await channel.send(f"{x}")
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        message = f'bot has left {guild}'
        channel = self.client.get_channel(845245176888688660)
        await channel.send(message)
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        #if message.author.bot == True:
        #    return
        if message.channel.id == 845245176888688660 or message.channel.id == 865789884035498004:
            return
        print(f" \"{message.content}\" was sent by {message.author} and later deleted in the server {message.guild}")
        message = f" \"{message.content}\" was sent by {message.author} and later deleted in the channel {message.channel} of the server {message.guild}"
        channel = self.client.get_channel(865789884035498004)
        await channel.send(message)
       
    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        if message_before.channel.id == 845245176888688660 or message_before.channel.id == 865789884035498004:
            return
        me = f"``{message_before.content}`` was changed to ``{message_after.content}`` by {message_before.author.name} in the channel {message_before.channel} of the server {message_before.channel.guild}"
        chan = self.client.get_channel(874221498225819648)
        await chan.send(me)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #await member.send(f'hola!')
        print(f'{member} joined {member.guild}')
        channel = self.client.get_channel(845245176888688660)
        #await channel.send(f'{member} joined {member.guild}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        message = f'{member} left from {member.guild}'
        channel = self.client.get_channel(845245176888688660)
        #await channel.send(message)
        
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        chan = self.client.get_channel(845245176888688660)
        await chan.send(f"{member} was banned from {guild}")
        
    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        channel = self.client.get_channel(845245176888688660)
        await channel.send(f"{member} was unbanned from {guild}")
        
    def ask():
        list.append(tuple([a])) # make a dictionary instead of list  
        print(list)

    #@commands.Cog.listener()
    #async def on_member_join(member):
    #    await member.send(f'Please provide your Date of Birth, we will use it to greet you on your birthday; if you dont wanna.... type "no".')
    #    await member.send(f'If u decide to provide your date of birth, please follow the following format: DD/MM')
    #    try:
    #        if response.content.lower() == "no": 
    #            await member.send(f'Alright!')
    #            await member.send(f'Have a good day ahead and Stay Safe!')
    #        if response.content.lower().replace('/','').isnum() == True:
    #            a = response.content.lower()
    #            while True :
    #                ask()
    #                a = datetime.datetime.today()
    #                for i in list:
    #                    if a.strftime("%Y/%m/%d") == i : 
    #                        await member.send(f"Happy Birthday {member}, Enjoy your day!") 
    #                    time.sleep(60*60*24)
    #    except: print('failed!')
            
        
    #commands

    @commands.command()
    async def hello(self, ctx):
        """Greets you"""
        await ctx.send(f'Hey there.')
       
        
    
    @commands.command()
    async def coloured(self, ctx, role1 : discord.Role, role2 : discord.Role, role3 : discord.Role, user : discord.Member=None, number=10):
        """Use this to make your name have 3 colors defined by the roles that you ping. 
        (Idea for this command was given by orb_server)"""
        user = user or ctx.author
        roles = [role1, role2, role3]
        for i in range(number):
            for j in roles:
                await user.add_roles(j)
                await asyncio.sleep(1)
                await user.remove_roles(j)
                await asyncio.sleep(2)
    
    
                
                
                
    @commands.command(aliases=["pfp"])
    async def avatar(self, ctx, user : discord.Member = None):
        user = user or ctx.author
        pp = user.avatar_url
        embed=discord.Embed(title=f"{user}'s Avatar", description='', color=0x270de7)
        embed.set_image(url=(pp))
        await ctx.send(embed=embed)
     
    #@commands.has_role("Strong Nuclear Force")
    #@commands.command(hidden=True)
    async def profile(self, ctx, user : discord.Member = None):
        user = user or ctx.author
        embed=discord.Embed(title=f"{user.display_name}",discription="",color=discord.Color.blue())
        embed.set_author(name=f"{user.name}",icon_url=user.avatar_url)
        embed.add_field(name="Username:",value=f"")
        
        
        
        
    @commands.command(name="invite", aliases=["bot invite link", "bot link"])
    async def _invite(self, ctx):
        """Generate an invite link to invite this bot to your server"""
        ur = 'https://discord.com/api/oauth2/authorize?client_id=784473379183788055&permissions=8&scope=bot%20applications.commands'
        
        omg = 'Have fun using this bot and contact the owner of the server SINUSOIDS if you face any incovenience.'
        embed = discord.Embed(title="Invite Link", url=ur, color=discord.Color.blurple())
        embed.set_footer(text=omg)
        m = f"{ctx.message.author.name} generated an invite link in {ctx.message.guild}"
        ch = self.client.get_channel(845245176888688660)
        await ch.send(m)
        
        await ctx.send(embed=embed,
                      components=[
                      Button(style=ButtonStyle.URL, label="Invite!", url="https://discord.com/api/oauth2/authorize?client_id=784473379183788055&permissions=8&scope=bot%20applications.commands")
                      ],
                      )
        r = await self.client.wait_for("button_click")
        if r.channel == ctx.channel:
            await ch.send(m)
           
        
    @commands.command(name="upvote", aliases=["vote", "vote for bot", "upvote bot"])
    async def _upvote(self, ctx):
        """Vote for me !!!"""
        embed = discord.Embed(title="Vote for Pegasus",color=discord.Color.green())
        #embed.add_field(name="Vote on top.gg !",value="https://top.gg/bot/784473379183788055")
        #embed.add_field(name="Vote on Discord Bot List!",value="https://discordbotlist.com/bots/upsilon/upvote")
        embed.set_thumbnail(url=("https://cdn.discordapp.com/attachments/784494481159618560/849999269628346398/ucandoit.gif"))
        await ctx.send(embed=embed)
        
        await ctx.send(
            "Help us grow!",
            components=[
                [Button(style=ButtonStyle.URL,label="top.gg",url="https://top.gg/bot/784473379183788055"),
                Button(style=ButtonStyle.URL,label="discordbotlist.com",url="https://discordbotlist.com/bots/upsilon/upvote")]
            ],
        )
        res = await self.client.wait_for("button_click")


    @commands.command(name="quote")
    async def _quote(self, ctx):
        """generates a randome quote"""
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(embed = discord.Embed(title=f"{quote}", color=discord.Color.blurple()))

        
        
    @commands.command()
    async def physics(self, ctx):
        """creates an embed with a link for the science blog -- deltapsifi"""
        embed=discord.Embed(title="A science blog", url="https://deltapsifi.com/", description="A place to learn about various concepts in the fields of Quantum Mechanics, Particle Physics, and Math.", color=0x3c08f7)
        embed.set_author(name="??????", url="https://deltapsifi.com/")
        embed.add_field(name="Click on the link above", value="And make sure to follow the blog in order to get updates directly in your inbox", inline=False)
        embed.set_footer(text="Here one can even talk about various theories in the field of science.")
        await ctx.send(embed=embed)
        
        
        
    @commands.command()
    async def cs(self, ctx):
        """creates an embed with a link for the computer science blog -- hackolympus"""
        embed=discord.Embed(title="A computer science blog", url="https://hackolympus.com/", description="A place to learn about various concepts in the fields of cyber security, linux and many more. ", color=0x3c08f7)
        embed.set_author(name="Zeus", url="https://hackolympus.com/")
        embed.add_field(name="Click on the link above", value="And make sure to follow the blog in order to get updates directly in your inbox", inline=False)
        embed.set_footer(text="it also has various CTFs")
        await ctx.send(embed=embed)
      
   
        
        
    @commands.command(name="support", aliases=["support server", "support invite"])
    async def _support(self, ctx):
        """creates an embed with an invite link for the support server of this bot"""
        embed=discord.Embed(title="A wonderful server for Science and Computer Science", url="https://discord.gg/aXVWmDxRmF", description="A great place for discussion, collaboration, getting your doubts cleared and learning new things on a variety of topics like quantum mechanics, quantum computing, astrophysics and many more. ", color=0x08f738)
        embed.set_author(name="SINUSOIDS", url="https://discord.gg/aXVWmDxRmF")
        embed.add_field(name="https://discord.gg/aXVWmDxRmF      ", value="Click on the server name to join the server and please share this invite link.", inline=False)
        embed.set_footer(text="This server was created with the idea that knowledge must be accessible to and attainable by all individuals for free.")
        await ctx.send(embed=embed)
   

    @commands.command(name="server", aliases=["server invite", "server link"])
    async def _server(self, ctx):
        """Generates an invite link to the server the bot is in."""
        embed=discord.Embed(title=f"Server Invite Link:", url=f'{await ctx.channel.create_invite(max_age="300")}', description=f"{await ctx.channel.create_invite(max_age='300')}", color=discord.Color.purple())
        embed.set_author(name=f"{ctx.channel.guild.name}")
        embed.set_image(url=(f"{ctx.channel.guild.icon_url}"))
        embed.add_field(name="Server Description:", value=f"{ctx.channel.guild.description}", inline=True)
        embed.add_field(name=f"Owner:", value=f"{ctx.channel.guild.owner}", inline=True)
        embed.add_field(name=f"Member Count:", value=f"{ctx.channel.guild.member_count}", inline=True)
        embed.add_field(name=f"Created At:", value=f"{ctx.channel.guild.created_at}", inline=True)
        embed.add_field(name="Server Link:", value=f'{await ctx.channel.create_invite(max_age="300")}')
        await ctx.send(embed=embed)
      
  
    


    
    
#    @commands.command()
#    async def sn(self, ctx):
#        await ctx.send(f'{server.name}')
    
    
    
          
        
#board = Board()
#board.legal_moves

#class Chess(commands.Cog):
    
#    def __init__(self, client):
#        self.client = client

#    @commands.Cog.listener()
#    async def on_ready(self):
#        print('chess is working')
#
#    def Get_Picture(self, color):
#        flipped = color == "black"
#        svg_data = chess.svg.board(self.board, flipped = flipped)
#        cairosvg.svg2png(bytestring=svg_data, write_to = "output.png")
        
        
#    def Take_Turn(self):
#        self.white.turn = not self.white.turn
#        self.black.turn = not self.black.turn
        
        
        
#    @commands.command()
 #   async def currentposition(self, color):
  #      await self.client.say('Current board position:')
   #     Get_Picture(color)
        
#    @commands.command(pass_context=True)
 #   async def playchess(self, ctx, name = ''):
  #      if self.white != '' and self.black != '':
   #         return await ctx.send(f'There is already a game being played on this server')
    #    if len(ctx.message.mentions) == 0:
     #       return await ctx.send(f'You must mention another player to start a game.')
      #  if len(ctx.message.mentions) > 1:
       #     return await self.client.say('You are mentioning too many people')
        #if ctx.message.mentions[0] == ctx.message.author:
         #   return await self.client.say('You cannot play against yourself!')

#        author = ctx.message.author
 #       opponent = ctx.message.mentions[0]
  #      rand = random.randrange(0,2)
   #     self.white = Player('white', author) if rand == 0 else Player('white', opponent.name + "#" +  opponent.discriminator)
    #    self.black = Player('black', author) if rand != 0 else Player('black', opponent.name + "#" + opponent.discriminator)
#        self.white.turn = True
 #       self.Get_Picture('white')
  #      await self.client.send_file(ctx.message.channel, fp = 'output.png')
   #     await self.client.send_message(ctx.message.channel, 'Your move, {}'.format(self.white.username))
        
        
    #@commands.command(pass_context=True)
#    async def move(self, ctx, move = ''):
#        """Make your move"""
#        if self.white == '' and self.black == '':
#            await ctx.send(f'There is no active game available')
#        if move == '':
#            await self.client.send('You must supply a move')
#        player = self.white if self.white.turn == True else self.black
#        logging.warning(player.username)
#        logging.warning(ctx.message.author)
#        if str(ctx.message.author) != str(player.username):
#            return await self.client.send_message(ctx.message.channel, 'It is not your turn, {}'.format(ctx.message.author))
#        else:
#            try:
#                self.board.push_san(move)
#                self.Take_Turn()
#                color = "white" if player != self.white else "black"
#                nextuser = self.white.username if player != self.white else self.black.username
#                self.Get_Picture(color)
#                if self.board.is_game_over() == True:
#                    await self.client.send_file(ctx.message.channel, fp = 'output.png')
#                    await self.client.send_message(ctx.message.channel, 'Game over. {}'.format(self.board.result()))
#                    self.Reset()
#                else:
#                    await self.client.send_file(ctx.message.channel, fp = 'output.png')
#                    await self.client.send_message(ctx.message.channel, 'Your move, {}'.format(nextuser))
#            except ValueError:
#                await self.client.send_message(ctx.message.channel, '{} is an illegal move, {}'.format(move, ctx.message.author))

#    @commands.command()
#    async def board(self, ctx):
#        """shows the board"""
#        await self.client.send_file(ctx.message.channel, fp = 'output.png')

#    @commands.command()
#    async def exit(self, ctx):
#        """Only use this if the other person is cheating or making you wait too long.
#        Misuse will result in ban from the server."""
#        board.reset()
#        await ctx.send(f'Die in Hell')

#    @commands.command()
#    async def result(self, ctx):
#        """get the game result and end game"""
#        await ctx.send(board.result())
#        board.reset()
    
    

 

def setup(client):
    client.add_cog(Function(client))
    #client.add_cog(Chess(client))
