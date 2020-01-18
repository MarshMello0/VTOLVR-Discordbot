import discord
from discord.ext import commands

token = open("BotLogin.txt").read()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot has logged in")

client.run(token)