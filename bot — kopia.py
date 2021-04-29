import discord
from discord.ext import commands,tasks
import os
import time
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import has_permissions, CheckFailure

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', help_command=None,intents=intents)

@client.event
async def on_ready():
    print('Zalogowano na {0.user} \n'.format(client))

@client.command()
async def dm(ctx):
    message = 'Witamy cie na w naszej Ekipie, mamy nadzieję, że dobrze się będziesz bawić'

    true = 0
    false = 0
    for user in client.get_all_members():
        try:
            await user.send(message)
            print('wyslano wiadomosc do ' + str(user) + '\n')
            true += 1

        except:
            print('nie mozna wyslac wiadomosci do ' + str(user) + '\n')
            false += 1 
        
        time.sleep(2)

    print('dobre ' + str(true) + ' zle ' + str(false))


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
    em2 = discord.Embed(title=f"Pong!",description=f"Twój ping wynosi {round(client.latency * 1000)}ms")
    await ctx.send(embed=em2)
    
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
    await ctx.send('Aktualne komendy to:')
    await ctx.send('$ping')
    await ctx.send('$Kanał (podaje kanały aktualnych właścicieli)')   

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def Kanał(ctx):
    await ctx.send('https://www.youtube.com/channel/UCzngNEq47RSgscsXdxFRGOw')

    time.sleep(1)
    await ctx.send('https://www.youtube.com/channel/UCfNC9ow_d1lrUiPYo4m8tLw')

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def kanał(ctx):
    await ctx.send('https://www.youtube.com/channel/UCzngNEq47RSgscsXdxFRGOw')

    time.sleep(1)
    await ctx.send('https://www.youtube.com/channel/UCfNC9ow_d1lrUiPYo4m8tLw')

@ping.error
async def ping_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Poczekaj chwile!",description=f"Spróbuj ponownie za {error.retry_after:.2f}s.", color=31)
        await ctx.send(embed=em)

@kanał.error
async def kanał_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Poczekaj chwile!",description=f"Spróbuj ponownie za {error.retry_after:.2f}s.", color=31)
        await ctx.send(embed=em)

@Kanał.error
async def Kanał_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Poczekaj chwile!",description=f"Spróbuj ponownie za {error.retry_after:.2f}s.", color=31)
        await ctx.send(embed=em)

@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Poczekaj chwile!",description=f"Spróbuj ponownie za {error.retry_after:.2f}s.", color=31)
        await ctx.send(embed=em)


#@ping.error
#async def ping_error(ctx, error):
    #if isinstance(error, commands.CommandOnCooldown):
        #em = discord.Embed(title=f"Poczekaj chwile!",description=f"Spróbuj ponownie za {error.retry_after:.2f}s.", color=31)
        #await ctx.send(embed=em)

client.run('ODM3MDc5ODU4MTY0NzkzMzQ0.YInVXg.jsld3L6SQ8JQUPR-rPdprUEfoO4')
