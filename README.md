### Twitch-Chat

📜 I made an script in Python for receive message from twitch chat.

## Tutorial 💻

For use the bot, make sure to do this:

```py
class Bot(commands.Bot):

    def __init__(self):
        # Make sure to put your personal token, use https://twitchapps.com/tmi/ for generate a random token.
        super().__init__(token='tokenbot', prefix='?', initial_channels=['channelname'])

bot = Bot()
bot.run()
```

And if you wanna make the chat, add this event:

```py
class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token='tokenbot', prefix='?', initial_channels=['channelname'])
    async def event_message(self, ctx: commands.Context):
        # Print author and content of message
        print(f"From {ctx.author.name}: {ctx.content}")

bot = Bot()
bot.run()
```

And now, you can run the script and you'll have message content and message's author !


## Wanna contact us ? 🤔

If you wanna contact us, send mail at miyucode@gmail.com
