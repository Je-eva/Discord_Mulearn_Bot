import discord
from discord.ext import commands
#/ is command prefix, ie, it means the message is for bot
mubot=commands.Bot(command_prefix="!",intents=discord.Intents.default())
#intents=discord.Intents.all()

#discord.com/channels/1188181623867445288/1205319065267347506
@mubot.event
async def on_ready():
    print("The bot is ready to use")
    print("**********")
#responding to particular message(command) 

mubot.command()
async def hello(ctx):
    await ctx.send("Hello i am the discord bot")

@mubot.command()
async def sad(ctx):
    await ctx.send("Hello i am sad")

@mubot.event
async def on_member_join(member):
    welcome_channel = mubot.get_channel(1205319065267347506)
    message=f"WELCOME to server: {member.name}"
    await welcome_channel.send(message)#group mesg 
    await member.send(message)#dm     
    
@mubot.event

async def on_message(message):
    if message.author.bot:
        return 
    await message.reply("roger that")
    await message.channel.send("nothing happenning")
    await message.author.send("good jbo")
    await message.add_reaction("😭")
mubot.run(decouple.config("DISCORD_TOKEN"))

