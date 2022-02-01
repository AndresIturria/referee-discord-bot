import load, utilities, random, db
import discord
from discord.ext import commands


if __name__ == '__main__':

    async def get_discord_username(ctx, id):
        try:
            killer_member = await ctx.guild.fetch_member(id)
            return killer_member.display_name
        except(discord.errors.NotFound):
            return("This user is not in the server")

    # Load messages and images and Discord token
    warning_img, yellow_img, red_img, expulsion_img, trapcard_img = load.load_imgs()
    error_warnings, error_yellows, error_reds, error_expulsions, error_generic, msg_greeting, \
        msg_coin_winner, msg_coin_loser = load.load_messages()
    TOKEN = load.load_token()

    bot = commands.Bot(command_prefix="$")


    @bot.command(
        help="Greeting",
        brief="Greeting"
    )
    async def referee(ctx, *args):
        if len(args) > 0:
            await ctx.channel.send(random.choice(error_generic))
        else:
            await ctx.channel.send(random.choice(msg_greeting))


    @bot.command(
        help="Turn vowels into i's",
        brief="Turn vowels into i's"
    )
    async def msgi(ctx, *args):
        if len(args) == 0:
            await ctx.channel.send(random.choice(error_generic))

        else:
            content = ""
            for arg in args:
                content = content + " " + arg

            response = ""
            for char in content:
                if char in "aeouAEOU":
                    response += "i"

                else:
                    response += char

            await ctx.channel.send(response)


    @bot.command(
        help="Head or Tails, type $coin head or $coin tails",
        brief="Head or Tails, type $coin head or $coin tails"
    )
    async def coin(ctx, *args):
        if len(args) > 1 or len(args) == 0:
            await ctx.channel.send(random.choice(error_generic))

        else:
            arg = args[0]
            if arg == 'head' or arg == 'tails':
                toss = random.randint(0, 1)
                choice = ""
                if toss == 0:
                    choice = 'head'
                else:
                    choice = 'tails'

                await ctx.channel.send(f"Result: {choice}")
                if arg == choice:
                    await ctx.channel.send(random.choice(msg_coin_winner))
                else:
                    await ctx.channel.send(random.choice(msg_coin_loser))

            else:
                await ctx.channel.send(random.choice(error_generic))


    @bot.command(
        help="Server leaderboard",
        brief="Server leaderboard"
    )
    async def leaderboard(ctx, *args):
        if len(args) > 0:
            await ctx.channel.send(random.choice(error_generic))

        else:
            server_id = ctx.guild.id
            top_warnings, top_yellows, top_reds, top_expulsions = db.get_leaderboard(server_id)

            embed1 = discord.Embed(title="Warnings", color=0x03f8fc)
            embed2 = discord.Embed(title="Yellow Cards", color=0x03f8fc)
            embed3 = discord.Embed(title="Red Cards", color=0x03f8fc)
            embed4 = discord.Embed(title="Expulsions", color=0x03f8fc)

            for user in top_warnings:
                member = await get_discord_username(ctx, user.userID)
                embed1.add_field(name=member, value=user.totalWarnings)

            for user in top_yellows:
                member = await get_discord_username(ctx, user.userID)
                embed2.add_field(name=member, value=user.totalYellows)

            for user in top_reds:
                member = await get_discord_username(ctx, user.userID)
                embed3.add_field(name=member, value=user.totalReds)

            for user in top_expulsions:
                member = await get_discord_username(ctx, user.userID)
                embed4.add_field(name=member, value=user.totalExpulsions)

            await ctx.channel.send(embed=embed1)
            await ctx.channel.send(embed=embed2)
            await ctx.channel.send(embed=embed3)
            await ctx.channel.send(embed=embed4)


    @bot.command(
        help="$warning @usuario",
        brief="$warning @usuario"
    )
    async def warning(ctx, *args):
        if len(args) > 1 or len(args) == 0:
            await ctx.channel.send(random.choice(error_warnings))

        else:
            userid = utilities.parse_userid(args[0])
            serverid = ctx.guild.id
            yellow, red = db.warning(userid, serverid)

            if red:
                member = await ctx.guild.fetch_member(userid)
                await discord.Member.move_to(member, None, reason="red card")
                await ctx.channel.send(random.choice(red_img))

            elif yellow:

                await ctx.channel.send(random.choice(yellow_img))

            else:

                await ctx.channel.send(random.choice(warning_img))


    @bot.command(
        help="$yellow @usuario",
        brief="$yellow @usuario"
    )
    async def yellow(ctx, *args):
        if len(args) > 1 or len(args) == 0:
            await ctx.channel.send(random.choice(error_yellows))

        else:
            userid = utilities.parse_userid(args[0])
            serverid = ctx.guild.id
            red_check = db.yellow(userid, serverid)

            if red_check:

                member = await ctx.guild.fetch_member(userid)
                await discord.Member.move_to(member, None, reason="red card")
                await ctx.channel.send(random.choice(red_img))

            else:

                await ctx.channel.send(random.choice(yellow_img))


    @bot.command(
        help="$red @usuario",
        brief="$red @usuario"
    )
    async def red(ctx, *args):
        if len(args) > 1 or len(args) == 0:
            await ctx.channel.send(random.choice(error_reds))

        else:
            userid = utilities.parse_userid(args[0])
            serverid = ctx.guild.id
            db.red(userid, serverid)
            member = await ctx.guild.fetch_member(userid)
            await discord.Member.move_to(member, None, reason="red card")
            await ctx.channel.send(random.choice(red_img))

    @bot.command(
        help="$expulsion @usuario",
        brief="$expulsion @usuario"
    )
    async def expulsion(ctx, *args):
        if len(args) > 1 or len(args) == 0:
            await ctx.channel.send(random.choice(error_expulsions))

        else:
            userid = utilities.parse_userid(args[0])
            serverid = ctx.guild.id
            # trapcard
            try:
                if userid == int(330050931716521985):
                    userid = ctx.author.id
                    db.expulsion(userid, serverid)
                    member = await ctx.guild.fetch_member(userid)
                    await discord.Member.kick(member, None, reason="Bye")
                    await ctx.channel.send(random.choice(trapcard_img))

                else:
                    db.expulsion(userid, serverid)
                    member = await ctx.guild.fetch_member(userid)
                    await discord.Member.kick(member, None, reason="Bye")
                    await ctx.channel.send(random.choice(expulsion_img))

            except:
                await ctx.channel.send(random.choice(error_expulsions))


    @bot.event
    async def on_ready():
        print('Online')
    bot.run(TOKEN)










