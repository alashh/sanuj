import discord
from discord.ext import commands
from passcode import token

bot = commands.Bot(command_prefix='qilbot ', description='My test bed for random python bots and what they do')

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
        author_truncated = str(message.author).partition("#")[0]
        await bot.send_message(message.channel, "New Lobby Added to list: {} By: {}#{} timestamp: {}".format(message.content, author_truncated, message.channel, message.timestamp))

bot.run(token)
