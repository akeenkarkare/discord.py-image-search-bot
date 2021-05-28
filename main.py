import discord
from discord.ext import commands
from googleapiclient.discovery import build
import random

client = commands.Bot(command_prefix="!")
api_key = "insert google api key here"


@client.event
async def on_ready():
    print("bot online.\n")


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = #random.randint(0, 0) #(use this only if you have the upgraded version of the google api)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="custom browser code here", searchType="image"
    ).execute()
    url = result["items"][0]["link"]
    embed1 = discord.Embed(title=f"Here is the image you wanted: ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


client.run("custom bot token here")
