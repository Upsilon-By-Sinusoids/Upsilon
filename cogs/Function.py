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

#profanity.load_censor_words_from_file("bannedwords.txt")

client = discord.Client


class Function(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        
    #@commands.Cog.listener()
    #async def on_message(message):
    #    if message.content.startswith('owner')
    #        await message.send(f'message.guild.owner_id')
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f'{guild} joined by bot')
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f'bot has left {guild}')
  

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #await member.send(f'hola!')
        print(f'{member} joined {member.guild}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} left from {member.guild}')
        
        
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
            
        
        
#    @commands.Cog.listener()
#    async def on_message_delete(message):
#        msg = str(message.author)+ 'deleted message in '+str(message.channel)+': '+str(message.content)
#        await ctx.channel.send(f'{msg}')

    #commands

    @commands.command()
    async def hello(self, ctx):
        """Greets you"""
        await ctx.send(f'Hey there.')

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def clear(self, ctx, amount=10):
        """This commands can be used for bulk message deletion, the default value is 10; however, you can delete as many as you want"""
        await ctx.channel.purge(limit=amount+1)
        
    @commands.has_role("Strong Nuclear Force")
    @commands.command()
    async def servers(self, ctx):
        """This command is exclusively for the owner of Upsilon"""
        member = "ΔΨφ#6251"
        for guild in list(client.fetch_guilds):
            #channel = await member.create_dm()
            print(guild)
            #await channel.send(guild)
            
    @commands.has_role("Strong Nuclear Force")
    @commands.command()
    async def profile(self, ctx, user : discord.Member = None):
        await ctx.send(fetch_user_profile(user.id))
        
    @commands.command()
    async def invite(self, ctx):
        """Generate an invite link to invite this bot to your server"""
        await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=784473379183788055&permissions=4294442871&scope=bot')
        time.sleep(0.2)
        await ctx.send(f'Have fun using this bot and contact the owner of the server SINUSOIDS if you face any incovenience.')
        

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def nuke(self, ctx, channel: discord.TextChannel):
        try:
            await channel.delete()
            await ctx.send(f'A nuke has been dropped on #{channel}')
        except:
            await ctx.send(f'Why were u trying to delete a channel 🤨')
            
    """@commands.command()
    async def spam(self, ctx):
        i = 0
        while i<10:
            i+=1
            await ctx.send(f'Python for Jihad @Nitin#2929')"""

    """@commands.command()
    async def bump(self, ctx):
        await ctx.send(f'!d bump')"""

    """@commands.command()
    async def meme(self, ctx):
        await ctx.send(f'pls meme')
        for j in range(20):
            time.sleep(8)
            await ctx.send(f'pls meme')"""

    @commands.command()
    async def quote(self, ctx):
        """generates a randome quote"""
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)

    @commands.command()
    async def physics(self, ctx):
        """creates an embed with a link for the science blog -- deltapsifi"""
        embed=discord.Embed(title="A science blog", url="https://deltapsifi.com/", description="A place to learn about various concepts in the fields of Quantum Mechanics, Particle Physics, and Math.", color=0x3c08f7)
        embed.set_author(name="ΔΨφ", url="https://deltapsifi.com/")
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
        
    @commands.command()
    async def server(self, ctx):
        """creates an embed with an invite link for the support server of this bot"""
        embed=discord.Embed(title="A wonderful server for Science and Computer Science", url="https://discord.gg/aXVWmDxRmF", description="A great place for discussion, collaboration, getting your doubts cleared and learning new things on a variety of topics like quantum mechanics, quantum computing, astrophysics and many more. ", color=0x08f738)
        embed.set_author(name="SINUSOIDS", url="https://discord.gg/aXVWmDxRmF")
        embed.add_field(name="https://discord.gg/aXVWmDxRmF      ", value="Click on the server name to join the server and please share this invite link.", inline=False)
        embed.set_footer(text="This server was created with the idea that knowledge must be accessible to and attainable by all individuals for free.")
        await ctx.send(embed=embed)

    #@commands.command()
    #async def linkserver(self, ctx):
    #    embed=discord.Embed(title="A growing community of nerds.", url="https://discord.gg/CJ7epwcGtc", description="Place for nerds to find peace, balance, meaning, knowledge & ideas. Social, science, classical music, opera, classic films, comics, eyebleach, movies, fantasy, scifi  & general nerdy things. Is a SFW server.", color=0x270de7)
    #    embed.set_author(name="Corner of the Universe", url="https://discord.gg/CJ7epwcGtc")
    #    embed.add_field(name="https://discord.gg/CJ7epwcGtc ", value="Click on the server name to join the server and please share this invite link.", inline=False)
    #    await ctx.send(embed=embed)

    
    
    
    
    
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
    #client.add_cog(Moderation(client))
    #client.add_cog(Music(client))
    #client.add_cog(Chess(client))
