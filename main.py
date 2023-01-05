# import os
# import discord

# intents = discord.Intents.default()
# intents.message_content = True

# client  = discord.Client(intents=intents)

# my_secret = os.environ['TOKEN']

# @client.event
# async def on_ready():
#   print(f"We have logged in as {client.user}")

# @client.event
# async def on_message(msg):
#   if msg.author == client.user:
#     return

#   if msg.content.startswith('$hello'):
#     await msg.channel.send('Hello!')

# client.run(my_secret)

import bot

if __name__ == '__main__':
    bot.run_discord_bot()
