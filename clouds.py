import os
import discord
from discord.ext import commands
import asyncio
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash import client
from discord_slash.utils.manage_commands import create_option
from discord import channel, utils
import random
from discord.ext.commands import bot
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from discord.ext import commands
from discord.ext.commands.core import command

client = commands.Bot(command_prefix="^", intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    client.load_extension("bumper")
    print("Ready!")

guild_ids = [799526257506254868, 730269125028610118]


@slash.slash(name="ping", description="Ping Pong Me", guild_ids=guild_ids)
async def _ping(ctx):
    await ctx.send(f"Pong! `{round(client.latency *1000)}ms`")
client.sniped_messages = {}


@client.event
async def on_message_delete(message):
    if message.author != 813313220739334185:
        client.sniped_messages[message.channel.id] = (
            message.content, message.author, message.channel.name, message.created_at)
        await asyncio.sleep(40)
        client.sniped_messages[message.channel.id] = None


@slash.slash(name="snipe", description="Snipes the deleted message", guild_ids=guild_ids)
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.channel.id]
        embed = discord.Embed(description=contents,
                              color=0x2f3136, timestamp=time)
        embed.set_author(
            name=f'{author.name}#{author.discriminator}', icon_url=author.avatar_url)
        embed.set_footer(text=f'Deleted in: #{channel_name}')
        await ctx.send(embed=embed, delete_after=60)
    except:
        await ctx.send("Do you want me to snipe air?", delete_after=60)
client.esniped_messages = {}


@client.event
async def on_message_edit(before, after):
    if after.author.id != 813313220739334185:
        client.esniped_messages[before.channel.id] = (
            before.content, before.author, before.channel.name, before.created_at)
        print(client.esniped_messages)
        await asyncio.sleep(40)
        client.esniped_messages[before.channel.id] = None


@slash.slash(name='esnipe', description='Snipes the edited message', guild_ids=guild_ids)
async def esnipe(ctx):
    try:
        contents, author, channel_name, time = client.esniped_messages[ctx.channel.id]
        embed = discord.Embed(description=contents,
                              color=0x2f3136, timestamp=time)
        embed.set_author(
            name=f'{author.name}#{author.discriminator}', icon_url=author.avatar_url)
        embed.set_footer(text=f'Edited: #{channel_name}')
        await ctx.send(embed=embed)

    except:
        await ctx.send("*Do you want me to snipe air?*", delete_after=60)


@slash.slash(name='PP', description='Ofc I measures your pp what else', options=[
    create_option(
        name="member",
        description="why do you want to know about other's pp?",
        option_type=6,
        required=False
    )
], guild_ids=guild_ids)
async def pp(ctx, member: discord.Member = None):
    x = random.randint(1, 20)
    y = "8"
    d = "D"
    c = y+"="*x+d
    if member is None:
        member = ctx.author.name

        if x <= 10:
            z = (f''' Your PP Size..
      is **{c}** ''')
            em = discord.Embed(title=" Peepee Sizer - smol ",
                               description=f'{z}', color=0x2f3136)
            await ctx.send(embed=em)
        else:
            z = (f''' Your PP Size..
          **{c}**  ''')
            em = discord.Embed(title=" Peepee Sizer - big ",
                               description=f'{z}', color=0x2f3136)
            await ctx.send(embed=em)
    else:
        if x <= 10:
            z = (f''' {member.name}'s PP Size..
          **{c}** ''')
            em = discord.Embed(title="Peepee Sizer - smol",
                               description=f'{z}', color=0x2f3136)
            await ctx.send(embed=em)

        else:

            z = (f'''{member.name}'s Your PP Size..
          **{c}** ''')
            em = discord.Embed(title="Peepee Sizer - big",
                               description=f'{z}', color=0x2f3136)
            await ctx.send(embed=em)


@slash.slash(name='howhorny', description='can you stop being horny', options=[
    create_option(
        name="member",
        description="Damn you saucy ew",
        option_type=6,
        required=False
    )
], guild_ids=guild_ids)
async def horny(ctx, member: discord.Member = None):
    x = random.randint(1, 100)
    if member is None:
        member = ctx.author.name
        await ctx.send(f'<:hornyass:854657133539098675> **You** are **{x}**% horny')

    else:
        await ctx.send(f'<:hornyass:854657133539098675> **{member.name}** is **{x}**% horny')


@slash.slash(name='howgay', description='See how gay ye are', options=[
    create_option(
        name="member",
        description="Choose a person",
        option_type=6,
        required=False
    )
], guild_ids=guild_ids)
async def gay(ctx, member: discord.Member = None):
    x = random.randint(1, 100)
    if member is None:
        member = ctx.author.name
        await ctx.send(f'<a:homo:835055067337588746> **You** are **{x}**% Gay')

    else:
        await ctx.send(f'<a:homo:835055067337588746> **{member.name}** is **{x}**% Gay')


@slash.slash(name='eightball', description='If you dont know something ask me!', options=[
    create_option(
        name="ask",
        description="Just ask it pftt",
        option_type=3,
        required=True
    )
], guild_ids=guild_ids)
async def eiball(ctx, ask: None):

    ba = ["Ask Me If I Care", "Dumb Question Ask Another", "Forget About It", "In Your Dreams", "Not A Chance", "ofc", " yeasss", "I'd say yes but you have to get me some crack B)", "You may rely on it", "Obviously", "What Do You Think?",  "Who Cares?", "You've Got To Be Kidding",
          "Yeah Right", " You Wish", "Absolutely", "Unclear Ask Later", "Chances Aren't Good", "Ask <@261742964441612298> the Coolest Person here", "Indications Say Yes", "No Doubt About It", "The Stars Say No", "You Can Count On It", "Ask <@533696842613915658> the lozer"]

    content = discord.Embed(
        color=0x2f3136, description="<:mmLol:825380160765034507> {}".format(random.choice(ba)))
    await ctx.send(embed=content)


@slash.slash(name='emergencyping', description='For emergency situations that needs staff', options=[
    create_option(
        name="reason",
        description="mention the reason",
        option_type=3,
        required=True
    )
], guild_ids=guild_ids)
async def emergency(ctx, reason: None):
    if reason is not None:
        em = discord.Embed(title="Emergency Ping", colour=0x2f3136)

        em.add_field(name="Reason:", value=f"```{reason}```", inline=False)
        em.add_field(name="Triggered by:",
                     value=f"<@{ctx.author.id}> - `{ctx.author.id}`", inline=True)

        x = "<@&742501744206020798>"
        m = await ctx.send(x, embed=em)
        await m.add_reaction("<:emergency_ping:831873364087537664>")


@slash.slash(name='howsimpy', description='See how simpy ye are', options=[
    create_option(
                  name="member",
        description="you can see how simpy others are!",
        option_type=6,
        required=False
    )
], guild_ids=guild_ids)
async def gay(ctx, member: discord.Member = None):
    x = random.randint(1, 100)
    if member is None:
        member = ctx.author.name
        await ctx.send(f'**You** are **{x}**% Simpy')

    else:
        await ctx.send(f'**{member.name}** is **{x}**% Simpy')


@slash.slash(name='howstinky', description='Go take a shower ffs', options=[
    create_option(
                  name="member",
        description="I can sniff for you!",
        option_type=6,
        required=False
    )
], guild_ids=guild_ids)
async def stinky(ctx, member: discord.Member = None):
    x = random.randint(1, 100)
    if member is None:
        member = ctx.author.name
        await ctx.send(f'<:trashcan:750152850310561853> **You** are **{x}**% Stinky')

    else:
        await ctx.send(f'<:trashcan:750152850310561853> **{member.name}** is **{x}**% Stinky')


@slash.slash(name='howweeby', description='uhm i can sense how weeby you are', options=[
    create_option(
                  name="member",
        description="I can sniff for you!",
        option_type=6,
        required=False
    )
], guild_ids=guild_ids)
async def stinky(ctx, member: discord.Member = None):
    x = random.randint(1, 100)
    if member is None:
        member = ctx.author.name
        await ctx.send(f'<a:animesip:855069282936160277> **You** are **{x}**% Weeby')

    else:
        await ctx.send(f'<a:animesip:855069282936160277> **{member.name}** is **{x}**% Weeby')


@slash.slash(name='poll', description='Start a poll', options=[

    create_option(
                  name="message",
        description="mention the reason",
        option_type=3,
        required=True
    ),
    create_option(
        name="choice1",
        description="enter your choice",
        option_type=3,
        required=True
    ), create_option(
        name="choice2",
        description="enter your choice",
        option_type=3,
        required=True
    ), create_option(
        name="choice3",
        description="enter your choice",
        option_type=3,
        required=False), create_option(
        name="choice4",
        description="enter your choice",
        option_type=3,
        required=False)
], guild_ids=guild_ids)
@slash.permission(guild_id=799526257506254868,
                  permissions=[
                      create_permission(730275055854157865,
                                        SlashCommandPermissionType.ROLE, True),
                      create_permission(879246928246882304,
                                        SlashCommandPermissionType.ROLE, True),

                  ])
async def poll(ctx, message, choice1, choice2, choice3=None, choice4=None):
    c = 0
    if choice4 is not None:
        x = f'''
<:one:855099025446404096> {choice1}

<:two:855099024923033621> {choice2}

<:three:855099025460428832> {choice3}

<:four:855099025292001341> {choice4}'''
        c = 4
    elif choice3 is not None:
        x = f'''
<:one:855099025446404096>  {choice1}

<:two:855099024923033621>  {choice2}

<:three:855099025460428832>  {choice3} '''
        c = 3
    else:
        x = f'''
<:one:855099025446404096>  {choice1}

<:two:855099024923033621>  {choice2}'''
        c = 2
    em = discord.Embed(title=f'{message}', description=f'{x}', color=0x5865F2)
    m = await ctx.send(embed=em)
    for x in range(1, c+1):

        if c == 2:
            await m.add_reaction('<:one:855099025446404096>')
            await m.add_reaction('<:two:855099024923033621>')
        elif c == 3:
            await m.add_reaction('<:one:855099025446404096>')
            await m.add_reaction('<:two:855099024923033621>')
            await m.add_reaction('<:three:855099025460428832>')
        elif c == 4:
            await m.add_reaction('<:one:855099025446404096>')
            await m.add_reaction('<:two:855099024923033621>')
            await m.add_reaction('<:three:855099025460428832>')
            await m.add_reaction('<:four:855099025292001341>')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):

    Content = discord.Embed(
        color=0x2f3136, description=f"Banned **{member.name}#{member.discriminator}** \n Reason - {reason}")
    Content.set_footer(text=f'Banned by {ctx.author.name}',
                       icon_url='https://cdn.discordapp.com/emojis/915795784690196530.png?size=40')
    await member.ban(reason=reason)


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            Content = discord.Embed(
                color=0x2f3136, description=f"Unbanned {user.id}")
            Content.set_footer(
                text=f'Unbanned by {ctx.author.name}', icon_url='https://cdn.discordapp.com/emojis/915795784690196530.png?size=40')
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    Content = discord.Embed(
        color=0x2f3136, description=f"Kicked **{member.name}#{member.discriminator}** \n Reason - {reason}")
    Content.set_footer(text=f'Kicked by {ctx.author.name}',
                       icon_url='https://cdn.discordapp.com/emojis/915795784690196530.png?size=40')

    await member.kick(reason=reason)


client.run(os.environ['DISCORD_TOKEN'])
