import traceback
from mongoengine import *
import sys

from configparser import ConfigParser  
from tabulate import tabulate
from datetime import datetime

import asyncio
import discord
from discord.ext import commands

from utils import *
from models import Member


#Main connection function offered by mongoengine defaults are localhost:27017
connect(db_name)

bot = commands.Bot(command_prefix='gsbot ', description=description)

#Here check for server configs and add a new collection for each server name
def check_server_config():
    pass


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    check_server_config()
    # Here we load our extensions listed above in [initial_extensions].
    if __name__ == '__main__':
        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
                print('loaded {}'.format(extension))
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await bot.send_message(ctx.message.author, 'This command cannot be used in private messages.')
    elif isinstance(error, commands.DisabledCommand):
        await bot.send_message(ctx.message.author, 'Sorry. This command is disabled and cannot be used.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await bot.send_message(ctx.message.channel, codify("Does not compute: try gsbot help or gsbot help <specific command>"))
    elif isinstance(error, commands.CommandNotFound):
        await bot.send_message(ctx.message.channel, codify("I don't know that command: try gsbot help"))

bot.run(token)
