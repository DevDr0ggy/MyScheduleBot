import discord
from discord.ext import commands
import datetime
import pytz
import os
from dotenv import load_dotenv

# Load environment variables from the hidden .env file
load_dotenv()

# Set up bot intents (Required for reading messages)
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # Sync slash commands (/) when the bot starts
    try:
        synced = await bot.tree.sync()
        print(f"Bot is online! Logged in as {bot.user}")
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Command for Monday schedule
@bot.tree.command(name="monday", description="Show schedule for Monday")
async def monday(interaction: discord.Interaction):
    msg = (
        "**ตารางเรียนวันจันทร์:**\n"
        "⏰ 09:00 - 12:00 น.\n"
        "📚 ใส่ชื่อวิชา... \n"
        "🏢 ห้องเรียน... \n"
    )
    await interaction.response.send_message(msg)

# ==========================================
# ชัยก๊อปปี้โค้ดคำสั่ง @bot.tree.command ของวันอังคาร-ศุกร์ ของเดิมมาวางต่อตรงนี้ได้เลยครับ!
# ==========================================

# Fetch the token from the OS environment and run the bot
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if DISCORD_TOKEN is None:
    print("Error: DISCORD_TOKEN not found! Please check your .env file.")
else:
    bot.run(DISCORD_TOKEN)