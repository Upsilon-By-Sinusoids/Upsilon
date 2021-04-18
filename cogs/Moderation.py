






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
                print(message.content)
                await message.channel.send(choice)
                await message.delete()
                
                
    @commands.has_permissions(kick_members=True) 
    @commands.command()
    async def kick(self, ctx, Member: discord.Member):
        await bot.kick(Member)
