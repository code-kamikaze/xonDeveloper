import random
import discord
import asyncio
import os
import dbdmusic

@client.event
async def on_ready():
    print(f"bot is ready")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('.ping en mantenimiento bot por ekian'))

@client.command(help = "para saber cuanta lactancia tienes")
async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(0.5)
    await ctx.send(f'Pong! {round(client.latency * 100)}ms')
