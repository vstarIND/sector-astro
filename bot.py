import discord
import matplotlib.pyplot as plt
import random
import asyncio
import datetime
from discord.ext import commands

TOKEN = "MTMzNDE5NjAwNDExOTEyMTk2MQ.GV000x.rgA-VCRvC4d-TNOPZhE4q-KYBAUEkgwhLsm1qg"
CHANNEL_ID = 1353797313067221055

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def generate_graph(prices, timestamps):
    plt.figure(figsize=(6, 3))
    plt.plot(timestamps, prices, color='green', linewidth=2)
    plt.xlabel("Time")
    plt.ylabel("Price (INR)")
    plt.title("Live Price Graph")
    plt.grid()
    plt.xticks(rotation=45)
    plt.savefig("graph.png")
    plt.close()

async def live_graph(channel):
    set_price = 2.00  # Fixed price at 2:00 PM
    prices = []
    timestamps = []
    start_time = datetime.datetime.now()
    
    while True:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        fluctuation = random.uniform(-0.01, 0.01)
        current_price = round(set_price + fluctuation, 2)
        
        prices.append(current_price)
        timestamps.append(current_time)
        
        generate_graph(prices, timestamps)
        
        with open("graph.png", "rb") as file:
            picture = discord.File(file)
            await channel.send(file=picture)
        
        await asyncio.sleep(0.05)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await live_graph(channel)
    else:
        print("Channel not found!")

bot.run(TOKEN)
