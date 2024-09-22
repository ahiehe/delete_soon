import discord
from discord.ext import commands
import random
from botLogic import *

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! " + ctx.message.author.name)

@bot.command()
async def toss(ctx):
    await ctx.send(toss_coin())

@bot.command()
async def gpass(ctx, *args):
    await ctx.send(pass_gen(int(args[0])))   

@bot.command()
async def repeat(ctx, content, times = 5):
    for i in range(times):
        await ctx.send(content)


bot.run("MTI4NDc3NDEwMzUwMDMyNDg3Ng.G6u8YH.fSb_FF4oqU1sDD2Su5M0EjqZ_wIiI6EubvYdr8")
