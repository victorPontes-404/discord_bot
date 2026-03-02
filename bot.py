import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def is_owner(ctx):
    return ctx.author.id == OWNER_ID

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def status(ctx):
    if not is_owner(ctx):
        return
    
    import subprocess
    
    uptime = subprocess.check_output("uptime -p", shell=True).decode()
    ram = subprocess.check_output("free -h", shell=True).decode()
    disk = subprocess.check_output("df -h /", shell=True).decode()

    embed = discord.Embed(
        title="📊 Status do Servidor",
        color=0x00ff00
    )

    embed.add_field(name="⏳ Uptime", value=f"```{uptime}```", inline=False)
    embed.add_field(name="🧠 RAM", value=f"```{ram}```", inline=False)
    embed.add_field(name="💾 Disco", value=f"```{disk}```", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)