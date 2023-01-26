import discord
import os
from dotenv import load_dotenv
from lemat_control import MyClient

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(BOT_TOKEN)
