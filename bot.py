import discord
from discord.ext import commands

botData = open("BotData.txt").readlines()
token = 'TOKEN'
welcomeID = 0
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('vtolvr-mods.com'))
    print("Bot has logged in")

@client.event
async def on_member_join(member):
    print(f"{member} joined the server")
    channel = client.get_channel(welcomeID)
    await channel.send(f'<@{member.id}>  has joined the server!')

@client.event
async def on_member_remove(member):
    print(f"{member} left the server")
    channel = client.get_channel(welcomeID)
    await channel.send(f'{member}  has left the server')


@client.event
async def on_message(message):
    lowercase = message.content.lower()
    channel = message.channel
    if ("when" in lowercase and "next" in lowercase and "test" in lowercase):
        await channel.send("If you are asking about when the next multiplayer test will be, sadly there isn't planned dates for them. They just happen when its ready to be tested. Sorry.")
        return
    await client.process_commands(message)


for line in botData:
    result = line.strip()
    if ("TOKEN=" in result):
        token = result.replace("TOKEN=","")
        print(f"Token = {token}")
    elif  ("WELCOME=" in result):
        welcomeID = int(result.replace("WELCOME=",""))
        print(f"Welcome Channel ID = {welcomeID}")
    
client.run(token)