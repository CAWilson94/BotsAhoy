import aiohttp
import asyncio

import os
from discord.ext import commands
from token_bot import DAD_JOKE_TOKEN

bot = commands.Bot(command_prefix='!')

dad_joke_kingdom = "https://icanhazdadjoke.com/"
HEADERS = {"Accept": "application/json", "User-Agent": "Yer Maw"}

async def dad_jokko(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=dad_joke_kingdom, headers=HEADERS) as response_boi:             
            return await response_boi.json()

def dad_joke_runner():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())   
    bob = asyncio.run(dad_jokko())        
    print(bob['joke'])    

@bot.command(name='joke')
@commands.cooldown(1, 10, commands.BucketType.user)
async def dad_joke(ctx): 
    json = await dad_jokko()
    await ctx.send(json['joke'])


@bot.event
async def on_ready(): 
    print(f'{bot.user.name} has connected to Discord!')

bot.run(DAD_JOKE_TOKEN)