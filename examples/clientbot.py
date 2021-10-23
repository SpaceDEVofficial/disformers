import discord
from DisFormers import DisFormersBot

class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot is ready.")

    async def on_message(self,message):
        disformerbot = DisFormersBot(client, prefix="!")
        await disformerbot.client_message(message=message)

client = MyClient()

if __name__ == "__main__":
    client.run('token')