# This file is part of mariano-bot.
#
# mariano-bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mariano-bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mariano-bot. If not, see <http://www.gnu.org/licenses/>.

"""Koldrak Lair Event, notification and command.

This module contains Koldrak Lair notification and his related constants.
"""
import asyncio
from datetime import (datetime, time)

import discord
from discord.ext import commands

# Bot imports
import utils


EVENT_SCHEDULE = (
    (time(1, 0, 0), time(1, 0, 1)),
    (time(13, 0, 0), time(13, 0, 1)),
    (time(16, 0, 0), time(16, 0, 1)),
    (time(19, 0, 0), time(19, 0, 1)),
    (time(22, 0, 0), time(22, 0, 1))
)
PRESTART_MESSAGE = ("En 10 minutos podreis ir entrando a Koldrak. "
                    "Y recordad, si vais en party, pasad gemas; ¡que luego "
                    "hay que esperaros!")
START_MESSAGE = ("Teneis 10 minutos para entrar a Koldrak; a ver si "
                 "sois tan pros como para sacar el cofre premium, ¡COMO YO!")

# Embed
KOLDRAK_LAIR = discord.Embed(**{
    'title': 'Koldrak Lair',
    'description': 'Raid de 12 jugadores.',
    'colour': discord.Colour.gold()
})
KOLDRAK_LAIR.add_field(name='Time Zone', value='UTC', inline=False)
KOLDRAK_LAIR.add_field(name='Run 1', value='01:00')
KOLDRAK_LAIR.add_field(name='Run 2', value='13:00')
KOLDRAK_LAIR.add_field(name='Run 3', value='16:00')
KOLDRAK_LAIR.add_field(name='Run 4', value='19:00')
KOLDRAK_LAIR.add_field(name='Run 5', value='22:00')


@commands.command(pass_context=True)
async def koldrak(ctx):
    """Return Koldrak Lair Embed."""
    await ctx.bot.say(embed=KOLDRAK_LAIR)


async def event_koldrak_lair(bot):
    """Notify members when queue for Koldrak Lair are ready.

    Also send a message 10 minutes before queue are available.
    """
    await bot.wait_until_ready()

    while not bot.is_closed:
        for i in EVENT_SCHEDULE:
            # TIME INTERVAL
            # Case 1: 3.0 <= 2.0 <= 3.1 = (no, yes)
            # Case 2: 3.0 <= 4.0 <= 3.1 = (yes, no)
            # Case 3: 3.0 <= 3.022 <= 3.1 = (yes, yes)
            # Case 4: 3.0 <= 3.0 <= 3.1 = (yes, yes)
            # Case 5: 3.0 <= 3.1 <= 3.1 = (yes, yes)
            if i[0] <= datetime.now().time() <= i[1]:
                for s in bot.servers:
                    await utils.send_to_first_channel(bot, s, START_MESSAGE)
            # 10 minutes before queue are available
            elif (time(i[0].hour - 1, 50, 0) <= datetime.now().time()
                  <= time(i[0].hour - 1, 50, 1)):
                for s in bot.servers:
                    await utils.send_to_first_channel(bot, s, PRESTART_MESSAGE)
        await asyncio.sleep(1)
