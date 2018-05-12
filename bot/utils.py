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

"""This module contains reusable code.

Functions:
    first_text_channel() -- Returns the first text channel in which the bot can
                            send messages.
    send_to_first_channel() -- Send a message to first text channel.
"""
import discord


def first_text_channel(server: discord.Server) -> discord.Channel:
    """Returns the first text channel in which the bot can send messages.

    Parameters:
        server (obj): discord.server

    Returns:
        discord.Channel: first text channel.
    """
    for c in server.channels:
        if (c.type is discord.ChannelType.text and
                c.permissions_for(server.me).send_messages):
            return c


async def send_to_first_channel(bot, server: discord.Server, message):
    """Send a message to the first text channel of a server."""
    c = first_text_channel(server)
    await bot.send_message(c, message)
