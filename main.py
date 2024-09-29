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
async def bothelp(ctx):
    await ctx.send("$hello - print hello\n$toss - toss a coin\n$gpass [number] - generate password\n$repeat [message] [times] - repeat [message] [times] times\n$joined [name] - show when [name] joined")
    
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
        
@bot.command()
async def randmem(ctx):
    picture = "images/" + random.choice(os.listdir("images"))
    with open(picture, 'rb') as mem:
        picture = discord.File(mem)
    await ctx.send(file=picture)

def get_rand_image_url(url, imageKeyjson):    
    res = requests.get(url)
    data = res.json()
    return data[imageKeyjson]


@bot.command('duck')
async def duck(ctx):

    image_url = get_rand_image_url('https://random-d.uk/api/random', 'url')
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    image_url = get_rand_image_url('https://some-random-api.com/animal/dog', 'image')
    await ctx.send(image_url)
    
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run(TOKEN)
