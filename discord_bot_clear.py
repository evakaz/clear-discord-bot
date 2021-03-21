import discord
from discord.ext import commands
import traceback

client = commands.Bot(command_prefix = '!')
intents = True

async def onClearAction(myCtx, myNumber:int = None):
    if myCtx.message.author.guild_permissions.manage_messages:
        try:
            if myNumber == None:
               await myCtx.send('Please enter an amount of messages you want to delete.')
            else:
                await myCtx.channel.purge(limit=myNumber)
                print('purge')
                await myCtx.send(f'Messages cleared by {myCtx.message.author.mention} {myNumber}.')
                print('purge 2')
        except Exception as e:
            traceback.print_exc() 
            await myCtx.send("I can't delete messages here.")
    else:
        await myCtx.send("You don't have the permission to use this command.")

@client.command('clear')
async def clear(ctx, number:int = None):
    return await onClearAction(ctx, number)

client.run('TOKEN')