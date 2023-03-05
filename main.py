import discord, random
from discord.ext import commands

TOKEN = "MTA4MjAzMzg0ODc0NzAzMjYxNw.GBNCwx.0qJWAz4-k_2NWhBjkGMl7oF-09fgLtYinJWT-A"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.command(name = "roll")
async def roll(ctx,num):
  for i in range(int(num)):
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6 : {d}")
@bot.command(name = "ask")
async def ask(ctx, *args)

bot.run(TOKEN)