import discord
from DisFormers import DisFormersBot

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is ready.")

client = MyClient()
DisFormersBot(client,prefix="!")

if __name__ == "__main__":
    client.run('token')