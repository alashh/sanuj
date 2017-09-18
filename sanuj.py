import discord
from discord.ext import commands
from passcode import token
from datetime import timedelta

bot = commands.Bot(command_prefix='qilbot ', description='My test bed for random python bots and what they do')
lobbies = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hello():
    """Replies with hello"""
    print("hello world in console")
    await bot.say("Hello!")

@bot.command()
async def lobby():
    """Replies with list of lobbies"""
    lobbysay = "Lobbies Listed Below: \n"
    loopnum = 0
    for single_lobby in lobbies:
        loopnum += 1
        lobbysay = lobbysay + "{}) {} :clock: \n".format(loopnum, single_lobby)
    await bot.say(lobbysay)

@bot.command()
async def techstuff():
    """Various technical troubleshooting info"""
    botname = bot.user
    botself = bot.user
    alivetime = localtime()
    await bot.say("My name is: {} \n My current raw lobby list is: {}".format(botname, lobbies, botself))


@bot.event
async def on_message(message):
    if message.content.startswith(r'steam://joinlobby/') and message.author != bot.user:
        lobbies.append("{}#{}: {} @ {}".format(str(message.author).partition("#")[0], message.channel, message.content, message.timestamp))
        print("New Lobby Added to list: {} By: {}#{} timestamp: {}".format(message.content, str(message.author).partition("#")[0], message.channel, message.timestamp))
        await bot.send_message(message.channel, "New Lobby Added to list: {} By: {}#{} timestamp: {}".format(message.content, str(message.author).partition("#")[0], message.channel, message.timestamp))
    await bot.process_commands(message)

bot.run(token)
