import discord
from discord.ext import commands
import random
from pepe import pepedatabase
from giphy import Gif
import fortnite


description = '''Meme bot for real memers'''
bot = commands.Bot(command_prefix='?', description=description)
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    if len(result) < 2000:
        await bot.say(result)
    else:
        await bot.say('Result is too long. Look it up on wolfram alpha or something Kappa')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='Pepo-Bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

@bot.command()
async def subtract(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left - right)

@bot.command()
async def randompepe():
    """Posts a random Pepe"""
    pepe = random.choice(pepedatabase)
    await bot.say(pepe)

@bot.command()
async def randomboi():
    """Posts a random dat boi"""
    boi = Gif('datboi', 50).random()
    await bot.say(boi)

@bot.command()
async def gif(term: str):
    """Searches for and posts a gif from giphy"""
    _gif = Gif(term, 50).random()
    await bot.say(_gif)

@bot.command()
async def fortnitestats(nickname,platform):
    """Posts lifetime stats from fortnitetracker.com
    Format: ?fortnitestats nickname platform"""
    responseraw = fortnite.fortniteTracker(nickname,platform)
    dick = responseraw.get("lifeTimeStats")
    responsedict = {item["key"]:item for item in dick}
    mp = responsedict.get("Matches Played")["value"]
    w = responsedict.get("Wins")["value"]
    wp = responsedict.get("Win%")["value"]
    k = responsedict.get("Kills")["value"]
    kd = responsedict.get("K/d")["value"]
    response = """{} playing Fortnite on {} lifetime stats:
Matches Played: {} Wins: {} Win %: {} Kills: {} K/D: {}
    """.format(nickname,platform,mp,w,wp,k,kd)
    await bot.say(response)