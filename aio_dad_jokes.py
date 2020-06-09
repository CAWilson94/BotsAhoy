import aiohttp
import asyncio

import os
from discord.ext import commands
from token_bot import DAD_JOKE_TOKEN

bot = commands.Bot(command_prefix='!')

dad_joke_kingdom = "https://icanhazdadjoke.com/"
shite_advice_kingdom = "https://api.adviceslip.com/advice"

HEADERS = {"Accept": "application/json", "User-Agent": "Yer Maw"}

async def dad_jokko(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=dad_joke_kingdom, headers=HEADERS) as response_boi:             
            return await response_boi.json()

async def shite_advice(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=shite_advice_kingdom, headers=HEADERS) as response_boi:             
            return await response_boi.json(content_type='text/html')


def dad_joke_runner():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())   
    bob = asyncio.run(dad_jokko())        
    print(bob['joke'])    

@bot.command(name='joke')
@commands.cooldown(1, 10, commands.BucketType.user)
async def dad_joke(ctx): 
    json = await dad_jokko()
    await ctx.send(json['joke'])

@bot.command(name='advice')
@commands.cooldown(1, 10, commands.BucketType.user)
async def advice_please(ctx): 
    json = await shite_advice()
    await ctx.send(json['slip']['advice'])


@bot.event
async def on_ready(): 
    print(f'{bot.user.name} has connected to Discord praise be!')

bot.run(DAD_JOKE_TOKEN)