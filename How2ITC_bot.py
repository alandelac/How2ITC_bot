# How2ITC_bot.py

# libreria para conectar el programa con discord
import discord

# el token de nuestro bot. DIFERENTE PARA CADA PERSONA
TOKEN = 'aqui pon tu token'

# cliente es la conexion con discord
client = discord.Client()

#aqui comprobamos si ya se conecto o no
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


# funcion para contestar mensajes
@client.event
async def on_message(message):

    # checa si el mensaje es de otro ususario, no de el mismo
    if message.author == client.user:
        return

    # depende de que le mandemos es la respuesta que nos da
    if message.content == 'Hola':
        response = 'Hola buenos dias.'
        await message.channel.send(response)

    elif message.content == 'Que tranza carnal':
        response = 'Como andamios'
        await message.channel.send(response)

    elif message.content == 'Qui hubo mirrey':
            response = 'Que pasa paps'
            await message.channel.send(response)

    else:
        response = 'no te entendi bro/sis'
        await message.channel.send(response)
        
client.run(TOKEN)
