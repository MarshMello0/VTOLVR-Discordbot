#!python3
import discord
import time
import os
from discord.ext import commands

print('Discord Bot Started, waiting 15 seconds')
time.sleep(15)
print('Finished waiting')

botData = open(os.path.dirname(os.path.abspath(__file__)) + os.sep + "BotData.txt").readlines()
token = 'TOKEN'
welcomeID = 0
serverID = 0
client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
    guild = client.get_guild(serverID)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(str(guild.member_count) + ' members!'))
    print("Bot has logged in")


@client.event
async def on_member_join(member):
    print(f"{member} joined the server")
    channel = client.get_channel(welcomeID)
    guild = client.get_guild(serverID)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(str(guild.member_count) + ' members!'))
    await channel.send(f'<@{member.id}>  has joined the server!')


@client.event
async def on_member_remove(member):
    print(f"{member} left the server")
    channel = client.get_channel(welcomeID)
    guild = client.get_guild(serverID)
    await channel.send(f'{member}  has left the server')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(str(guild.member_count) + ' members!'))


@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    lowercase = message.content.lower()
    channel = message.channel
    if ("when" in lowercase and "next" in lowercase and "test" in lowercase):
        await channel.send("If you are asking about when the next multiplayer test will be, sadly there isn't planned dates for them. They just happen when its ready to be tested. Sorry.")
        return
    if ("https://github.com/marshmello0/vtolvr-multiplayer" in lowercase):
        await channel.send("You've seem to have found the multiplayer mod repository. This isn't currently playable and is only there so people can easily contribute to it. Sorry.")
        return
    await client.process_commands(message)

@client.command()
async def addTester(ctx):
    if ("tester" in [y.name.lower() for y in ctx.author.roles]):
        await ctx.channel.send("You already have the role.\nIf you would like to remove it type ``.removeTester``")
    else:
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name="Tester")
        await ctx.author.add_roles(role)
        await ctx.channel.send(f"You've been given the tester role <@{ctx.author.id}>")

@client.command()
async def addtester(ctx):
    if ("tester" in [y.name.lower() for y in ctx.author.roles]):
        await ctx.channel.send("You already have the role.\nIf you would like to remove it type ``.removeTester``")
    else:
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name="Tester")
        await ctx.author.add_roles(role)
        await ctx.channel.send(f"You've been given the tester role <@{ctx.author.id}>")

@client.command()
async def removeTester(ctx):
    if ("tester" in [y.name.lower() for y in ctx.author.roles]):
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name="Tester")
        await ctx.channel.send(f'The tester role has been removed <@{member.id}>')
        await ctx.author.remove_roles(role)        
    else:
        await ctx.channel.send("You do not have the tester role, if you would like to become a tester for the multiplayer mod type ``.addTester``")

@client.command()
async def removetester(ctx):
    if ("tester" in [y.name.lower() for y in ctx.author.roles]):
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name="Tester")
        await ctx.channel.send(f'The tester role has been removed <@{member.id}>')
        await ctx.author.remove_roles(role)        
    else:
        await ctx.channel.send("You do not have the tester role, if you would like to become a tester for the multiplayer mod type ``.addTester``")

@client.command()
async def mptest(ctx, *user):
    if (len(user) is 1):
        await ctx.channel.send(f'{user[0]} there are no planned dates or times when multiplayer tests will happen.')
        await ctx.message.delete()
        return
    await ctx.message.delete()
    await ctx.channel.send("There are no planned dates or times when multiplayer tests will happen.")

@client.command()
async def stats(ctx):
    guild = client.get_guild(serverID)
    testerscount = 0
    for member in guild.members:
        if ("tester" in [y.name.lower() for y in member.roles]):
            testerscount = testerscount + 1
    await ctx.channel.send(str(guild.member_count) + " members"+ "\n" + str(testerscount) + " testers")

@client.command(aliases=['help'])
async def _help(ctx):
    await ctx.channel.send("Available commands\n``.addTester`` - Gives you the tester role\n``.removeTester`` - Removes the tester role\n``.help`` - Displays this message\n``.mptest`` - Displays the next mp test message\n``.stats`` - Displays the servers stats")

for line in botData:
    result = line.strip()
    if ("TOKEN=" in result):
        token = result.replace("TOKEN=", "")
    elif ("WELCOME=" in result):
        welcomeID = int(result.replace("WELCOME=", ""))
    elif ("GUILD=" in result):
        serverID = int(result.replace("GUILD=",""))

client.run(token)
