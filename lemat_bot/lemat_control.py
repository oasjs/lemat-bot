import discord
import os
from lemat import Lemat


lemat = Lemat()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.content.startswith('$karma'):
            channel = message.channel
            await channel.send(Lemat.formatted_spell_list(lemat))
            