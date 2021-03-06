import discord 
import requests
import spotipy
import dateutil.parser
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify()
scope = 'playlist-read-private'

class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Spotify is working')
        
    #@commands.command()
    #async def playlists(self, ctx, user: discord.Member = None):
    #    await ctx.send(f'{sp.current_user_playlists}')

    
    @commands.command()
    async def track(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        spt_res = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        
        await ctx.send(f'https://open.spotify.com/track/{spt_res.track_id}')
        
        if spt_res is None: 
            await ctx.send(f'{user} is not listening to Spotify')


        #IMAGES
        bg_img = Image.open('spotify.png')
        album_img = Image.open(requests.get(spt_res.album_cover_url, stream=True).raw).convert('RGBA')

        #FONTS
        font = ImageFont.truetype('debrosee.ttf', 16)
        font1 = ImageFont.truetype('dustfine.ttf', 14)
        font2 = ImageFont.truetype('AquireBold.otf', 14)
        font3 = ImageFont.truetype('oasis.ttf', 12)
        font4 = ImageFont.truetype('oasis.ttf', 12)

        #POS
        title_txt = 150, 30
        artist_txt = 150, 60
        album_txt = 150, 80
        start_txt = 150, 122
        dur_txt = 332, 125

        draw = ImageDraw.Draw(bg_img)
        draw.text(title_txt, spt_res.title, 'white', font=font)
        draw.text(artist_txt, f'by {spt_res.artist}', 'blue', font=font1)
        draw.text(album_txt, spt_res.album, 'white', font=font2)
        draw.text(start_txt, '0.0', 'white', font=font3)
        draw.text(dur_txt, f"{dateutil.parser.parse(str(spt_res.duration)).strftime('%M:%S')}",
         'white', font=font4)

        
        #COLOUR
        album_clr = album_img.getpixel((250, 100))
        bg_colour = Image.new('RGBA', bg_img.size, album_clr)
        bg_colour.paste(bg_img, (0,1), bg_img)

        album_image_re = album_img.resize((140,160))
        bg_colour.paste(album_image_re, (0,0), album_image_re)
    
        bg_colour.convert('RGB').save('spotify_clr.jpg', 'JPEG')

        await ctx.send(file=discord.File('spotify_clr.jpg'))


def setup(client):
    client.add_cog(Spotify(client))
