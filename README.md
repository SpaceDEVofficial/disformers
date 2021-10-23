# disformers
 Huggingface transformers for discord

# example
see [example](examples) folder

- use client
```python
import discord
from DisFormers import DisFormersBot

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is ready.")

client = MyClient()
DisFormersBot(client,prefix="!") 
#DisFormersBot(client,prefix="!",languague="en") default languague is English
# you can choose English(en) or Korean(ko) languague option

if __name__ == "__main__":
    client.run('token')
```

- use commands.Bot
```python
import discord
from discord.ext import commands
from DisFormers import DisFormersBot

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("Bot is ready.")


my_bot = MyBot(command_prefix="!", intents=discord.Intents.all())
DisFormersBot(my_bot,prefix="!")
#DisFormersBot(client,prefix="!",languague="en") default languague is English
# you can choose English(en) or Korean(ko) languague option

if __name__ == "__main__":
    my_bot.run("token")
```
