import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

with open("excuses.txt") as f:
    lines = f.readlines()

# lines = open("excuses.txt").read().splitlines()
myline =random.choice(lines)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def excuse(ctx):
    await ctx.send(myline)

@bot.command()
async def greet(ctx):
    await ctx.send(":middle_finger: :rage: ")

@bot.command()
async def livingston(ctx):
    await ctx.send("https://gfycat.com/unpleasantreliabledoe-ron-livingston")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Excuse Bot", description="Making excuses so you don't have to", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Captain Jack Rackham")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite", value="") # discord-bot invite link goes here

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Excuse Bot", description="Features:", color=0xeee657)

    embed.add_field(name="$excuse", value="Generates a random excuse from the excuses repository", inline=False)
        embed.add_field(name="$greet", value="The welcoming you deserve", inline=False)
    embed.add_field(name="$info", value="Bot info/statistics", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('') # token goes here

