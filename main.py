import discord
from discord.utils import get
import jishaku
from discord.ext import commands 
import datetime
#variables
#emojis
tick = '<a:Right:945939371784282112>'
redtick = '<a:RedTick:945939442856775740>'
enabled = '<:Enabled:973798736411103242>'
reply3 = '<:reply3:1003377442553081887> '
reply = '<:reply:991415922436886578> '
token = 'your token' 
prefix = '='
# note add your id or bot will not work
owner = [954314921208852511 , 992706007346196512]
intents = discord.Intents.all()
#main bot
client = commands.Bot(command_prefix = prefix, intents=intents)
client.owner_ids = owner
client.help_command = None
#online notification!

@client.event
async def on_ready():
    print(f'Connected: {client.user.id} | {client.user.name}')



# events
@client.listen('on_message')
async def mention(message):
    if client.user.mention in message.content.split():
        await message.reply("You can type `=help` for more info.")
    else:
        pass







#help 

@client.command()
async def help(ctx):
    embed = discord.Embed(color=0000, timestamp=datetime.datetime.utcnow())
    embed.add_field(name=f"{reply3} connect to voice channel", value=f"{reply} `{prefix}connect`", inline = False)
    embed.add_field(name=f"{reply3} leaves the voice channel", value=f"{reply} `{prefix}leave`", inline = False)
    embed.add_field(name=f"{reply3} stay 247 connected to voice channel", value=f"{reply} `{prefix}online (247)`", inline = False)
    embed.add_field(name=f"{reply3} shows owner commands", value=f"{reply} `{prefix} ownercommand`", inline = False)
    embed.set_footer(text = 'Note : This Bot Is Owner Only . Set Owner in source code', icon_url = "https://images-ext-1.discordapp.net/external/APiEDrYz2C8JSyompN88dExJzjprf8X5VHLYAJ69etI/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/954314921208852511/505f252494530b0a53851c1bc480577b.webp?width=465&height=465")
    await ctx.send(embed=embed)

# join vc

@client.command()
@commands.is_owner()
async def connect(ctx):

    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'**{tick} Joined: <#{channel.id}>**')





#leave vc

@client.command()
@commands.is_owner()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.guild.voice_client.disconnect() # Leave the channel
        await ctx.send(f'** {tick}Sucessfully Leaved <#{channel.id}>**')
    else:
        await ctx.send(f'**{reply3} Im Not Connected To A Voice Channel**')

#247

@client.command()
@commands.is_owner()
async def online(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.send(f'{enabled} 247 Enabled : <#{channel.id}>')
    else:
        await ctx.send(f'**{redtick} Im Not Connected To A Voice Channel**')





#add owner command
@client.command()
@commands.is_owner()
async def ownercommand(ctx):
    await ctx.send(f""" ```Owner Commands```
    {reply3} owners
    {reply3} ownerlist
    {reply3} loadjishaku
    {reply3} unloadjishaku""")

@client.command()
@commands.is_owner()
async def owners(ctx):
    await ctx.send(f'**{reply3}Total owners - {len(owner)} **')
@client.command()
@commands.is_owner()
async def ownerlist(ctx):
    await ctx.send(f'**{reply3}owners - {str(owner)} **')


@client.command()
@commands.is_owner()
async def loadjishaku(ctx):
    await client.load_extension('jishaku')
    await ctx.send(f' {tick} jishaku loaded')

@client.command()
@commands.is_owner()
async def unloadjishaku(ctx):
    await client.unload_extension('jishaku')
    await ctx.send(f'{tick} jishaku unloaded')

#enter your bot's tuken


client.run(token)    
