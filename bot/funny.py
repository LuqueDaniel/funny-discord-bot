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

"""Funny commands.

This module contains funny commands
"""
from discord.ext import commands


@commands.command(pass_context=True)
async def ignorante(ctx, user):
    """This function send a meme to an user.

    Args:
        ctx: Bot Context
        user: User to notify
    """
    await ctx.bot.say(f"{user} ¡Ignorante de la vida!")
    await ctx.bot.send_file(ctx.message.channel,
                            "bot/static/img/mariano_ignorante.jpg")
