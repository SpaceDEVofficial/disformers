# disformers
 Huggingface transformers for discord

# install
```cmd
pip install -U disformers
```

# example
see [example](examples) folder

- use client
```python
import discord
from disformers.DisFormers import DisFormersBot

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is ready.")

    async def on_message(self,message):
        disformerbot = DisFormersBot(client, prefix="!")
        await disformerbot.client_message(message=message)

client = MyClient()

if __name__ == "__main__":
    client.run('token')
```

- use commands.Bot
```python
import discord
from discord.ext import commands
from disformers.DisFormers import DisFormersBot

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

# contact
- [Discord](https://discord.gg/Jk6VRvsnqa)
- [Email](mailto:support@spacedev.space)