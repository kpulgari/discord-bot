from discord.ext import commands
from dotenv import load_dotenv
import os
import random
import asyncio

# fix env variables and user input for quiz cmd

load_dotenv()

bot = commands.Bot(command_prefix='!')
bot.videos = [os.getenv('one'), os.getenv('two'),
'os.getenv('three')]
bot.happylist = []

allowed_commands = ['hello', 'goodbye', 'music', 'happy', 'sad', 'calc', 'rand', 'quiz']

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, " + ctx.author.display_name + "!")
    
@bot.command()
async def goodbye(ctx):
    await ctx.send("Goodbye, " + ctx.author.display_name + "!")

@bot.command()
async def music(ctx):
    await ctx.send(random.choice(bot.videos))

@bot.command()
async def happy(ctx, *, item):
    await ctx.send("Awesome!")
    bot.happylist.append(item)
    print(bot.happylist)

@bot.command()
async def sad(ctx):
    await ctx.send("Hope this makes you feel better!")
    await ctx.send(random.choice(bot.happylist))

@bot.command()
async def calc(ctx, x: float, fn, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    elif fn == '%':
        await ctx.send(x % y)
    else:
        await ctx.send("bad operand")

@bot.command()
async def rand(ctx, num_one: int, num_two: int):
    if num_one > num_two:
        await ctx.send("bad operand")
    else:
        await ctx.send(random.randint(num_one, num_two))

@bot.command()
async def quiz(ctx):
    one = random.randint(0, 5)
    two = random.randint(0, 5)
    ans = one + two
    await ctx.send(f"What is {one} + {two}?")

    def check(msg):
        return msg == ans
        
    msg = await bot.wait_for('message', check=check)
    if msg:
        await ctx.send("GOOD")
    else:
        await ctx.send("BAD")

@bot.command()
async def cmds(ctx):
    list = ''
    for num, cmd in enumerate(allowed_commands):
        list += str(num + 1) + ". " + cmd.title() + "\n"
    await ctx.send(list)

password = os.getenv('password')
bot.run(password)
