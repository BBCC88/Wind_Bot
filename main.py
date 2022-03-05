import os,keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix='&')
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
  print('Bot is ready',bot.user)

@bot.command()
async def Hello(ctx):
    channel = await ctx.author.create_dm()
    await channel.send('This is the first DM.')

keep_alive.keep_alive()
bot.run(my_secret)