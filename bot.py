import os
import discord
import asyncio
import random
import requests
from dotenv import load_dotenv

load_dotenv('.env')


response = requests.get("https://manan-api.herokuapp.com/bottle")
manan_bottle = response.json()

responseg = requests.get("https://manan-api.herokuapp.com/guitar")
manan_guitar = responseg.json()

responsew = requests.get("https://manan-api.herokuapp.com/waxing")
manan_wax = responsew.json()

responsew = requests.get("https://manan-api.herokuapp.com/memes")
manan_memes = responsew.json()


TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = (message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message} in channel {channel}')

    if message.author == client.user:
        return

    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}, do you want manan pics? type pics')

    if user_message.lower() == 'pics':
        await message.channel.send("Categories:\n-Bottle (bottle pics)\n-Guitar (guitar pics)\n-Waxing (waxing pics)\n-Memes (manan memes)\n")
    if user_message.lower() == 'bottle pics':
        await message.channel.send(manan_bottle['message'])
        await message.channel.send(manan_bottle['img'])

    if user_message.lower() == 'guitar pics':
        range12 = random.randint(0, 1)
        await message.channel.send(manan_guitar[range12]['message'])
        await message.channel.send(manan_guitar[range12]['img'])

    if user_message.lower() == 'waxing pics':
        range14 = random.randint(0, 3)
        await message.channel.send(manan_wax[range14]['message'])
        await message.channel.send(manan_wax[range14]['img'])

    if user_message.lower() == 'manan memes':
        range122 = random.randint(0, 1)
        await message.channel.send(manan_memes[range122]['message'])
        await message.channel.send(manan_memes[range122]['img'])

    if user_message.lower().startswith("manan safai"):
        msg = user_message.split()
        n = len(msg)
        num = int(msg[n-1])
        await message.channel.purge(limit=num+1)


client.run(TOKEN)
