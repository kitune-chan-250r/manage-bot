import discord
import asyncio
from discord.utils import get

TOKEN = "NjE0NzE2OTY2MDQ0ODI3Njgx.XWDmmw.Z0ancBa3Cv7AuLSVHKczwQRi-Js"
client = discord.Client()  

@client.event
async def on_ready():
	print(client.emojis)

client.run(TOKEN)