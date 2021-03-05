import discord
from discord.ext import commands
from discord.ext.commands import Bot

from config import info

import Data as d

bot = commands.Bot(command_prefix="?")

#moderations commands
@bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, member:discord.Member, time:int, reason):
    role = discord.utils.get(ctx.guild.roles,name="mute")
    emb = discord.Embed(title="мут", color=0xff0000)
    emb.add_field(name="Админ", value=ctx.message.author.mention, inline=False)
    emb.add_field(name="Нарушитель", value=member.mention, inline=False)
    emb.add_field(name="Причина", value=reason, inline=False)
    emb.add_field(name="Время мута", value=time, inline=False)

    await member.add_roles(role)
    await ctx.send(embed=emb)

@bot.command()
async def say(ctx, *args):
    await ctx.send(' '.join(args))

@bot.command()
async def test(ctx, id):
    print(id)
    data = d.get_user_data(d.get_user_page(id))
    emb = discord.Embed(
        title="Статистика",
        description="Кол-во боёв: **{0[4]}**\nПроцент побед: **{0[5]}**\nПроцент побед(взвод): **{0[6]}**\nСредний урон: **{0[7]}**\n\nРЭ: **{0[0]}**\nWN6: **{0[1]}**\nWN7: **{0[2]}**\nMGR: **{0[3]}**".format(data),
        color=0xff0000
    )

    await ctx.send(embed=emb)

bot.run(info["token"]) 