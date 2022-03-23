import os
import discord
from discord.ext import commands
from discord.ui import InputText, Modal, Button
import requests
from dotenv import load_dotenv
import random
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")

API_URL = "https://spellforgeapi.online/spells"


bot = discord.Bot()


@bot.slash_command(name="spell", guild_id=(822661824909672449))
async def show_spell(ctx, spell):

    """Search for a dnd Spell by name."""
    spell_response = requests.get(f"{API_URL}/{spell}")

    spell_data = spell_response.json()
    spell = discord.Embed(
        title=spell_data["name"], description=spell_data["description"])
    spell.add_field(name="level", value=spell_data["spell_level"], inline=True)
    spell.add_field(name="school", value="Conjuration", inline=True)
    spell.add_field(name="casting time", value=spell_data["casting_time"])
    spell.add_field(name="range or area", value=spell_data["range_or_area"])
    spell.add_field(name="Duration", value=spell_data["duration"], inline=True)
    await ctx.send(embed=spell)


@bot.slash_command(name="rolld20")
async def roll_d_twenty(ctx):
    num = random.randint(1, 20)
    await ctx.send("fYou rolled a, {num}!")

bot.run(TOKEN)
