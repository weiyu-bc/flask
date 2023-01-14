import discord
import responses
import os


async def send_message(msg, user_msg, is_private):
    try:
        response = responses.handle_response(msg,user_msg)
        await msg.author.send(response) if is_private else await msg.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.all()
    intents.typing = False
    intents.presences = False

    # for test
    my_secret = ''
    # for farm
    # my_secret = ''
    # my_secret = os.environ['TOKEN']

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running.")

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        username = msg.author
        user_msg = str(msg.content)
        channel = str(msg.channel)

        print(f"{username} said: {user_msg} at {channel}.")
        if user_msg.startswith('?') or user_msg.startswith('？'):

            await send_message(msg, user_msg, is_private=True)
        else:
            await send_message(msg, user_msg, is_private=False)

    client.run(my_secret)

