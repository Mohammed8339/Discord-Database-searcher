import discord
from discord.ext import commands
from discord import utils

token = ""

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def find(ctx, *, message):

    await ctx.send("STARTING, IF NOTHING POPS UP, IT MEANS THERE IS NO RESULTS. (cAse SenSiTIVe)")

    user = message

    db_data_list = []

    with open("text.txt", "r", encoding="utf-8") as t:
        readlines = t.readlines()
        for line in readlines:
            db_data_list.append(line)

    for i in db_data_list:
        if user in i:
            await ctx.send(i)
        else:
            print("user not found")

print("working")
bot.run(token)

