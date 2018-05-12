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

"""Translate command module.

This module contains translate command and his related constants.
"""
# Discord API
from discord.ext import commands
# Google translate API
import googletrans


# List of languages for 'list' command. Discord limit of 2000 characters
LANGUAGES_LIST = """Lista de idiomas disponibles:
**af** afrikaans   **sq** albanian   **am** amharic   **ar** arabic
**hy** armenian   **az** azerbaijani   **eu** basque   **be** belarusian
**bn** bengali   **bs** bosnian   **bg** bulgarian   **ca** catalan
**ceb** cebuano   **ny** chichewa   **da** danish   **zh-tw** chinese (traditional)
**co** corsican   **hr** croatian   **cs** czech   **zh-cn** chinese (simplified)
**nl** dutch   **en** english   **eo** esperanto   **et** estonian
**tl** filipino   **fi** finnish   **fr** french   **fy** frisian
**gl** galician   **ka** georgian   **de** german   **el** greek
**gu** gujarati   **ht** haitian creole   **ha** hausa   **haw** hawaiian
**iw** hebrew   **hi** hindi   **hmn** hmong   **hu** hungarian
**is** icelandic   **ig** igbo   **id** indonesian   **ga** irish
**it** italian   **ja** japanese   **jw** javanese   **kn** kannada
**kk** kazakh   **km** khmer   **ko** korean   **ku** kurdish (kurmanji)
**ky** kyrgyz   **lo** lao   **la** latin   **lv** latvian
**lt** lithuanian   **lb** luxembourgish   **mk** macedonian   **mg** malagasy
**ms** malay   **ml** malayalam   **mt** maltese   **mi** maori
**mr** marathi   **mn** mongolian   **he** Hebrew   **ne** nepali
**no** norwegian   **ps** pashto   **fa** persian   **pl** polish
**pt** portuguese   **pa** punjabi   **ro** romanian   **ru** russian
**sm** samoan   **gd** scots gaelic   **sr** serbian   **st** sesotho
**sn** shona   **sd** sindhi   **si** sinhala   **sk** slovak
**sl** slovenian   **so** somali   **es** spanish   **su** sundanese
**sw** swahili   **sv** swedish   **tg** tajik   **ta** tamil
**te** telugu   **th** thai   **tr** turkish   **uk** ukrainian
**ur** urdu   **uz** uzbek   **vi** vietnamese   **cy** welsh
**xh** xhosa   **yi** yiddish   **yo** yoruba   **zu** zulu
**fil** Filipino   **my** myanmar (burmese)
"""

# Command help (discord.py show it with !t help and !t !help)
HELP = """Puedo traducir:

Uso:
`!t [idioma] [texto a traducir]`

Puedes ver la lista de idiomas:
`!t list`

Ejemplo:
`!t es Hello World!`
"""

class Translator(object):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def t(self, ctx, dest, *args):
        """Command that return a translation.

        Args:
            ctx: Context.
            dest (str): (Required) Destination language.
            *args: (Required) Text to translate.
        """
        if dest.lower() == 'list':
            result = LANGUAGES_LIST
        else:
            tr = googletrans.Translator().translate(' '.join(args), dest=dest)
            result = f"{ctx.message.author.mention}\n`{tr.origin}`\n{tr.text}"
        await ctx.bot.say(result)


    @t.error
    async def t_error(self, ctx, error):
        """Error handler for t command."""
        await self.bot.say(HELP)
