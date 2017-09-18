import discord
from discord.ext import commands
from passcode import token

bot = commands.Bot(command_prefix='qilbot ', description='My test bed for random python bots and what they do')
# lobbies = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hello():
    """Replies with hello"""
    await bot.say("Hello!")

@bot.event
async def on_message(message):
    if message.content.startswith(r'steam://joinlobby/'):
        user = message.author
        newlobby = message.content
        # lobbies = lobbies.append(newlobby)
        await client.send_message(message.channel, "New Lobby Added to list: {} by {} ".format(newlobby, user))

bot.run(token)
