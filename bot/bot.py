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

"""mariano-bot base module."""
import os

# Discord API
import discord

# Bot imports
import funny
import koldrak_lair
import translate
import utils

# Configuration
TOKEN = os.environ['TOKEN']
DESCRIPTION = "Mariano Delgado, metrosexual y pensador."


# Create bot
bot = discord.ext.commands.Bot(command_prefix='!', description=DESCRIPTION)
bot.remove_command('help')  # Remove default help command
# Adds commands and events
# Commands
bot.add_cog(translate.Translator(bot))
bot.add_command(funny.ignorante)
bot.add_command(koldrak_lair.koldrak)
# Events
bot.loop.create_task(koldrak_lair.event_koldrak_lair(bot))  # CARE WITH IT


@bot.command()
async def mariano():
    await bot.say(f"""```{bot.description}

    Traducir:
        !t [idioma] [texto a traducir]
        Para más información usa !t help

    Comanods inutiles:
        !ignorante [usuario]
    ```""")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_server_join(server: discord.Server):
    """When bot joins a server, send a message with bot description."""
    await utils.send_to_first_channel(bot, server, bot.description)


if __name__ == '__main__':
    bot.run(TOKEN)
