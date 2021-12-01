from discord.embeds import Embed
from discord.ext import commands
from discord import channel, utils
import discord
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from discord.ext.commands import bot
import random
import discord
from discord.ext import commands


class bumper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        try:
            s = message.embeds

            z = s[0]

            y = z.description

            guild = self.bot.get_guild(730269125028610118)
            channel = guild.get_channel(730294145012203540)
            x = '''It's Bump Time! 
    Type **!d bump** to Support us'''

            if 'Bump done' in y:
                emd = discord.Embed(
                    description='<a:capoopoof:847413169995513916> *Drop a review about this server*  ***[here](https://disboard.org/review/create/730269125028610118)*** *if you want to support us*', color=0x2f3136)
                await message.reply(embed=emd)

                await asyncio.sleep(7200)
                em = discord.Embed(title='Discord Bump Reminder!',
                                   description=x, color=0x2f3136)
                em.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/824594210727395368/826412920766332998/B.gif')
                em.set_footer(text="MY CAPS LOCK IS STUCK ")
                await channel.send('<a:capoo_work:825020992609976380> <@&792268917405122560>', embed=em)
        except IndexError:
            return None


def setup(bot):
    bot.add_cog(bumper(bot))
