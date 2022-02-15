from twitchio.ext import commands
import pprint

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token='token', prefix='?', initial_channels=['channelname'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Connected on {self.nick} with success ! - Twitch Bot')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    async def event_message(self, ctx: commands.Context):
        print(f"From {ctx.author.name}: {ctx.content}")

bot = Bot()
bot.run()
