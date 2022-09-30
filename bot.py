import os

from discord import Client
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(Client):
    async def on_thread_update(self, before, after):
        if after.archived:
            await after.unarchive()


client = MyClient()
client.run(TOKEN)
