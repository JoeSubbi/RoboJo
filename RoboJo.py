# bot.py
import os
from datetime import date
import random

import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

#load environmnet variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

#update connection status
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='pick', help="When followed by a series of space seperated arguments will return a random argument")
async def pick(ctx, *args):
    if len(args)==0: await ctx.send('No arguments were given')
    else:
        response = random.choice(args)
        await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #passive behaviour
    #nice /meme
    if '69' in message.content or '420' in message.content:
        response = '***nice!***'
        await message.channel.send(response)

    #smh
    if 'smh' in message.content.lower():
        try:
            emoji = '<a:smh:766672187728986122>'
            await message.channel.send(emoji)
            #await message.add_reaction(discord.utils.get(message.guild.emojis, name='smh'))
        except Exception as e:
            print (e)

    #happy birthday
    if 'happy birthday' in message.content.lower() or 'happy birfday' in message.content.lower():
        await message.channel.send('**Happy Birthday!** 🎈🎉')

    await bot.process_commands(message)

    if len(message.attachments) > 0:
        if ((message.guild.id == 722772511460163615 and message.channel.id == 722772700732456961) or message.guild.id != 722772511460163615):

            try:
                upvote = '<:Updoot:722777693980196904>'
                downvote = '<:Downdoot:722779863970218047>'
                await message.add_reaction(upvote)
                await message.add_reaction(downvote)
            except Exception as e:
                print (e)
            #await message.add_reaction(':grinning:')


"""
    #birthdays
    #list birthdays
    if message.content[:6] == 'b!list':
        #read from file
        with open(GUILD+'birthdays.txt','r') as f:
            response = f.read()
            response = ('\n').join(response)
        
        #if there are no birthdays, inform the user, else add them to the list
        if len(response) == 0: await message.channel.send('There are no brithdays, add one using the command: b!add')
        else: await message.channel.send(response)
    
    #add birthdays
    if message.content[:5] == 'b!add':
        text = message.content.split(' ')
        name = text[1]
        date = text[2]

        with open(GUILD+'birthdays.txt','a') as f:
            f.write(name+' '+date)

        response = 'Added '+name+'s birthday on '+date
        await message.channel.send(response)
    
    #remove birthdays
    if message.content[:5] == 'b!rem':
        name = message.content[5:]
        if name[0] == ' ': name = name[1:]
        with open(GUILD+'birthdays.txt','r') as f:
            text = f.read().split('\n')
            text = [i.split(' ') for i in text]

            found = False
            for birthday in text:
                if birthday[0] == name:
                    text.pop(birthday)
                    found = True
                    break
            
            #inform user what is going on
            if not found: await message.channel.send(name+' Not found')
            else: await message.channel.send('removed '+name+'s birthday')
    """

bot.run(TOKEN)