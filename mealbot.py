# classbot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from runweb import RunWeb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send("Hi, I'm Meal Bot!")

@bot.command(name = "allergy")
async def allergy_check(ctx, dc, allergy):
    web = RunWeb()
    allergy_free = web.search(dc, allergy)
    
    if (len(allergy_free) == 0):
        await ctx.send(f"Sorry, there are no dishes at {dc.title()} that you can consume")
    else:
        foods = ""
        for food in allergy_free:
            foods = foods + food + "\n"
        await ctx.send("Items on the menu you can eat today: ")
        await ctx.send("Note: Listed foods are only those with explicit ingredients on the UC Davis Student Housing and Dining Services websites.")
        await ctx.send(foods)
    
bot.run(TOKEN)
