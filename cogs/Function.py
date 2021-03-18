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
import chess.svg
import cairo
import cairosvg
import logging

class Function(commands.Cog):

    def __init__(self, client):
        self.client = client

    #events
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
  

    @commands.Cog.listener()
    async def on_member_join(member):
        print(f'Welcome {member}, glad to see that you have joined the server. Head over to the #introduction channel and introduce yourself')

    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f'{member} has left the server.')

    #commands

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hey there.')

    @commands.command()
    @commands.has_any_role('Strong Nuclear Force', 'Captain', 'Commander - No. 1')
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_any_role('Captain', 'Strong Nuclear Force')
    async def nuke(self, ctx, channel: discord.TextChannel):
        try:
            await channel.delete()
            await ctx.send(f'A nuke has been dropped on #{channel}')
        except:
            await ctx.send(f'Why were u trying to delete channel 🤨')
            
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
        """creates an embed with an invite link for this server"""
        embed=discord.Embed(title="A wonderful server for Science and Computer Science", url="https://discord.gg/aXVWmDxRmF", description="A great place for discussion, collaboration, getting your doubts cleared and learning new things on a variety of topics like quantum mechanics, quantum computing, astrophysics and many more. ", color=0x08f738)
        embed.set_author(name="SINUSOIDS", url="https://discord.gg/aXVWmDxRmF")
        embed.add_field(name="https://discord.gg/aXVWmDxRmF      ", value="Click on the server name to join the server and please share this invite link.", inline=False)
        embed.set_footer(text="This server was created with the idea that knowledge must be accessible to  and attainable by all individuals for free.")
        await ctx.send(embed=embed)

    @commands.command()
    async def linkserver(self, ctx):
        embed=discord.Embed(title="A growing community of nerds.", url="https://discord.gg/CJ7epwcGtc", description="Place for nerds to find peace, balance, meaning, knowledge & ideas. Social, science, classical music, opera, classic films, comics, eyebleach, movies, fantasy, scifi  & general nerdy things. Is a SFW server.", color=0x270de7)
        embed.set_author(name="Corner of the Universe", url="https://discord.gg/CJ7epwcGtc")
        embed.add_field(name="https://discord.gg/CJ7epwcGtc ", value="Click on the server name to join the server and please share this invite link.", inline=False)
        await ctx.send(embed=embed)

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    """@commands.Cog.listener()
    async def on_message(self, message):
        x = open('bannedwords.txt', 'r')
        for i in x.readlines():
            if i == message.content:
                await ctx.send(f"{message.author.mention}, Refrain from sending inapropriate messages or you will be banned")
                await message.delete()
            else: 
                pass"""

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('bannedwords.txt','r') as f:
            bad_words = '|'.join(s for l in f for s in l.split())
            bad_word_checker = re.compile(bad_words).search
        if bad_word_checker(message.content):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, you've been a bad boy")
            await message.channel.send(f"{message.author.mention}, Refrain from sending inapropriate messages or you will be banned")
        else:
            pass
    
    
          
        
"""board = Board()
board.legal_moves
logging.basicConfig(level=logging.DEBUG)

class Chess(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    

    @commands.Cog.listener()
    async def on_ready(self):
        print('chess is working')

    def Get_Picture(self, color):
        flipped = color == "black"
        svg_data = chess.svg.board(self.board, flipped = flipped)
        cairosvg.svg2png(bytestring=svg_data, write_to = "output.png")
        
        
    def Take_Turn(self):
        self.white.turn = not self.white.turn
        self.black.turn = not self.black.turn
        
        
        
    @commands.command()
    async def currentposition(self, color):
        await self.client.say('Current board position:')
        Get_Picture(color)
        
    @commands.command(pass_context=True)
    async def playchess(self, ctx, name = ''):
        if self.white != '' and self.black != '':
            return await self.client.say('There is already a game being played on this server')
        if len(ctx.message.mentions) == 0:
            return await self.client.say('You must mention another player to start a game.')
        if len(ctx.message.mentions) > 1:
            return await self.client.say('You are mentioning too many people')
        if ctx.message.mentions[0] == ctx.message.author:
            return await self.client.say('You cannot play against yourself!')

        author = ctx.message.author
        opponent = ctx.message.mentions[0]
        rand = random.randrange(0,2)
        self.white = Player('white', author) if rand == 0 else Player('white', opponent.name + "#" +  opponent.discriminator)
        self.black = Player('black', author) if rand != 0 else Player('black', opponent.name + "#" + opponent.discriminator)
        self.white.turn = True
        self.Get_Picture('white')
        await self.client.send_file(ctx.message.channel, fp = 'output.png')
        await self.client.send_message(ctx.message.channel, 'Your move, {}'.format(self.white.username))
        
        
    @commands.command(pass_context=True)
    async def move(self, ctx, move = ''):
        """Make your move"""
        if self.white == '' and self.black == '':
            self.client.say('There is no active game available')
        if move == '':
            self.client.say('You must supply a move')
        player = self.white if self.white.turn == True else self.black
        logging.warning(player.username)
        logging.warning(ctx.message.author)
        if str(ctx.message.author) != str(player.username):
            return await self.client.send_message(ctx.message.channel, 'It is not your turn, {}'.format(ctx.message.author))
        else:
            try:
                self.board.push_san(move)
                self.Take_Turn()
                color = "white" if player != self.white else "black"
                nextuser = self.white.username if player != self.white else self.black.username
                self.Get_Picture(color)
                if self.board.is_game_over() == True:
                    await self.client.send_file(ctx.message.channel, fp = 'output.png')
                    await self.client.send_message(ctx.message.channel, 'Game over. {}'.format(self.board.result()))
                    self.Reset()
                else:
                    await self.client.send_file(ctx.message.channel, fp = 'output.png')
                    await self.client.send_message(ctx.message.channel, 'Your move, {}'.format(nextuser))
            except ValueError:
                await self.client.send_message(ctx.message.channel, '{} is an illegal move, {}'.format(move, ctx.message.author))

    @commands.command()
    async def board(self, ctx):
        """shows the board"""
        await self.bot.send_file(ctx.message.channel, fp = 'output.png')

    @commands.command()
    async def exit(self, ctx):
        """Only use this if the other person is cheating or making you wait too long.
        Misuse will result in ban from the server."""
        board.reset()
        await ctx.send(f'Die in Hell')

    @commands.command()
    async def result(self, ctx):
        """get the game result and end game"""
        await ctx.send(board.result())
        board.reset()
        
if __name__ == "__main__":
    chess1 = chess.Board()
    chess1.push_san('e4')
    svg_data = chess.svg.board(chess1, coordinates = False, flipped = False, style = chess.svg.DEFAULT_STYLE)
    cairosvg.svg2png(bytestring=svg_data, write_to="output2.png")
    chess2 = chess.Board()
    #chess2.svg.board(chess2)
    print(chess1)
    print(chess2)"""
    
    
logging.basicConfig(level=logging.DEBUG)
class Player:
    def __init__(self, color, username):
       self.color = color
       self.username = username
       self.turn = False
    def move(self, move):
        return
    def print(self):
        print(self.player)
        print(self.username)
        
if __name__ == "__main__":
    a = Player('white', 'adarsh')
    a.print()

class Game():
    def __init__(self, bot):
        self.board = chess.Board()
        self.white = ''
        self.black = ''
        self.bot = bot
    def Reset(self):
        self.white = ''
        self.black = ''
        self.board = chess.Board()
    def Get_Picture(self, color):
        flipped = color == "black"
        svg_data = chess.svg.board(self.board, flipped = flipped)
        cairosvg.svg2png(bytestring=svg_data, write_to = "output.png")
    def Take_Turn(self):
        self.white.turn = not self.white.turn
        self.black.turn = not self.black.turn
    @commands.command()
    async def test(self):
        print("////")
        await self.bot.say('test test')
    @commands.command()
    async def currentposition(self, color):
        await self.bot.say('Current board position:')
        Get_Picture(color)
    @commands.command(pass_context=True)
    async def playchess(self, ctx, name = ''):
        if self.white != '' and self.black != '':
            return await self.bot.say('There is already a game being played on this server')
        if len(ctx.message.mentions) == 0:
            return await self.bot.say('You must mention another player to start a game.')
        if len(ctx.message.mentions) > 1:
            return await self.bot.say('You are mentioning too many people')
        if ctx.message.mentions[0] == ctx.message.author:
            return await self.bot.say('You cannot play against yourself!')

        author = ctx.message.author
        opponent = ctx.message.mentions[0]
        rand = random.randrange(0,2)
        self.white = Player('white', author) if rand == 0 else Player('white', opponent.name + "#" +  opponent.discriminator)
        self.black = Player('black', author) if rand != 0 else Player('black', opponent.name + "#" + opponent.discriminator)
        self.white.turn = True
        self.Get_Picture('white')
        await self.bot.send_file(ctx.message.channel, fp = 'output.png')
        await self.bot.send_message(ctx.message.channel, 'Your move, {}'.format(self.white.username))
    @commands.command(pass_context=True)
    async def move(self, ctx, move = ''):
        if self.white == '' and self.black == '':
            self.bot.say('There is no active game available')
        if move == '':
            self.bot.say('You must supply a move')
        player = self.white if self.white.turn == True else self.black
        logging.warning(player.username)
        logging.warning(ctx.message.author)
        if str(ctx.message.author) != str(player.username):
            return await self.bot.send_message(ctx.message.channel, 'It is not your turn, {}'.format(ctx.message.author))
        else:
            try:
                self.board.push_san(move)
                self.Take_Turn()
                color = "white" if player != self.white else "black"
                nextuser = self.white.username if player != self.white else self.black.username
                self.Get_Picture(color)
                if self.board.is_game_over() == True:
                    await self.bot.send_file(ctx.message.channel, fp = 'output.png')
                    await self.bot.send_message(ctx.message.channel, 'Game over. {}'.format(self.board.result()))
                    self.Reset()
                else:
                    await self.bot.send_file(ctx.message.channel, fp = 'output.png')
                    await self.bot.send_message(ctx.message.channel, 'Your move, {}'.format(nextuser))
            except ValueError:
                await self.bot.send_message(ctx.message.channel, '{} is an illegal move, {}'.format(move, ctx.message.author))

def setup(bot):
    bot.add_cog(Game(bot))
        
if __name__ == "__main__":
    chess1 = chess.Board()
    chess1.push_san('e4')
    svg_data = chess.svg.board(chess1, coordinates = False, flipped = False, style = chess.svg.DEFAULT_STYLE)
    cairosvg.svg2png(bytestring=svg_data, write_to="output2.png")
    chess2 = chess.Board()
    #chess2.svg.board(chess2)
    print(chess1)
    print(chess2)    
    
    
    

youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, client: commands.Bot, ctx: commands.Context):
        self.client = client
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = client.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.client.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.client, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.client.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the bot to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    @commands.has_permissions(manage_guild=True)
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    @commands.has_permissions(manage_guild=True)
    async def _pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='resume')
    @commands.has_permissions(manage_guild=True)
    async def _resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='stop')
    @commands.has_permissions(manage_guild=True)
    async def _stop(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        ctx.voice_state.songs.clear()

        if not ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')

        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))

        else:
            await ctx.send('You have already voted to skip this song.')

    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """Loops the currently playing song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.client.loop)
            except YTDLError as e:
                await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                await ctx.send('Enqueued {}'.format(str(source)))

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')

def setup(client):
    client.add_cog(Function(client))
    client.add_cog(Moderation(client))
    #client.add_cog(VoiceError(Exception, client))
    #client.add_cog(YTDLError(Exception, client))
    #client.add_cog(YTDLSource(discord.PCMVolumeTransformer, client))
    #client.add_cog(Song(client))
    #client.add_cog(SongQueue(client))
    #client.add_cog(VoiceState(client))
    client.add_cog(Music(client))
    client.add_cog(Chess(client))
