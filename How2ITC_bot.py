# How2ITC_bot.py

import random

import discord

TOKEN = 'ODc2NTQ0Mzc1MzY5Mzg0MDM4.YRlnkA.qLDcW1YZ_XT5tsQ8ZAee-iJKnwE'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Bienvenidos a todos los nuevos integrantes excepto a {member.name}!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    saludos = [
        'Hola buenos dias.',
        'Como andamios',
        'Que pasa paps'
    ]

    if message.content == 'Hola':
        response = saludos[0]
        await message.channel.send(response)
    elif message.content == 'Que tranza carnal':
        response = saludos[1]
        await message.channel.send(response)
    elif message.content == 'Qui hubo mirrey':
            response = saludos[2]
            await message.channel.send(response)
    else:
        response = 'no te entendi bro/sis'
        await message.channel.send(response)
client.run(TOKEN)