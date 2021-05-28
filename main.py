import discord
from discord.ext import commands
from googleapiclient.discovery import build
import random

client = commands.Bot(command_prefix="!")
api_key = "AIzaSyDyXLcEU5FWo5zwzXHsNUZumTwxhgkEruo"


@client.event
async def on_ready():
    print("bot online.\n")


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = 0 #random.randint(0, 0)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="567e97207e38f771f", searchType="image"
    ).execute()
    url = result["items"][0]["link"]
    embed1 = discord.Embed(title=f"Here is the image your dumbass wanted: ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


client.run("ODQ3MDAwMTY2NzIzODc4OTYz.YK3sYA.EbOGmnA00hbLdbkg9WwmQUrqauk")
