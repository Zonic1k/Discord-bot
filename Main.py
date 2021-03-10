import discord
import random
import youtube_dl
import os
import time
import colorama
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps
from discord import File, User
import requests
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '$')

players = {}

os.system('cls')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(' Prefix = $ | TikTok : Invisiblebreezy'))
    print("Bot is Online")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

images = [
    'https://i.imgur.com/uT6wTzs.jpeg']
                                    

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def bomb(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Channel bombed')

@client.command(name='kick', pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
    await member.kick()
    await context.send('User ' + member.display_name + ' has been kicked.')


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.delete()
    await ctx.send(f'***___{member.id} | {member.name} | was banned! | Reason =  {reason}___***')


@client.command(name='unban')  # Might not need ()
async def _unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.message.delete()


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Fuck no.',
                 'Not a chance',
                 'Dont count on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == "bruh":
            await message.delete()
            await message.channel.send("https://i.imgur.com/uT6wTzs.jpeg")
    await client.process_commands(message)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command(aliases=['user', 'info'])
async def whois(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention, color = discord.Color.purple())
    embed.add_field(name = "ID", value = member.id , inline= True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url= ctx.author.avatar_url, text = f"requested by {ctx.author.name}")
    embed.add_field(name = "Roles: ", value = ", ".join([str(r.name) for r in member.roles]))
    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    await ctx.send("Thanks for wanting to use my bot !!! https://discord.com/api/oauth2/authorize?client_id=818344617321299978&permissions=0&scope=bot")

@client.command('quote', help='Add a quote to an image.')
async def on_quote(ctx, image, *, quote):
    if len(ctx.message.mentions) > 0:
        im = Image.open(requests.get(ctx.message.mentions[0].avatar_url, stream=True).raw)
    else:
        im = Image.open(requests.get(image, stream=True).raw)
    im = ImageOps.expand(im, border=40, fill=(0,0,0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("FONTS/arial.ttf", 36)
    draw.text((10,0),quote,(255,255,255),font=font)
    im.save('temp-quote.png')
    with open('temp-quote.png', 'rb') as f:
        picture = File(f)
        await ctx.message.delete()
        await ctx.send(file=picture)
    os.remove('temp-quote.png')


@client.command(pass_context=True)
async def cmd(ctx):
    author = ctx.message.author

    embed = discord.Embed(color = discord.Color.blue())

    embed.set_author(name='Prefix = $')
    embed.add_field(name='cmd', value='List all commands',inline=False)
    embed.add_field(name='8ball', value='Test your fate',inline=False)
    embed.add_field(name='whois', value='Get info on a person',inline=False)
    embed.add_field(name='Invite', value='Invite the bot to your server!',inline=False)
    embed.add_field(name='kick', value='Remove someone from the server -mods',inline=False)
    embed.add_field(name='bomb', value='Clear chat only for -mods',inline=False)
    embed.add_field(name='ban', value='Ban someone from the server -Admin',inline=False)
    embed.add_field(name='Donate', value='You do not need to donate but if you want to support me here is my paypal! paypal.me/badgreenx',inline=False)
    embed.set_footer(text='Made by Invisiblebreezy5234')
    await ctx.message.delete()
    await ctx.send(embed=embed)



client.run('ODE4MzQ0NjE3MzIxMjk5OTc4.YEWs0A.FdFNosN6_CuIk9EFfteOC3WdccE')
