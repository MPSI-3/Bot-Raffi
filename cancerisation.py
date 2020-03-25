# bot.py
import os

import discord
from dotenv import load_dotenv

from random import randint

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('Raffi paré au combat !'.format(client))

    
# Lorsque le bot lit un message avec la syllabe "di" dedans, il envoie un
# message contenant le reste de la phrase
def blague_di(content, index):
    return content[index+2:]
def blague_cri(content, index):
    return content[index+3:].upper()
def blague_quoi(content, index):
    return "feur"
def blague_comment(content, index):
    return "tateur"
def blague_chapiro(content, index):
    R = ["chapiteau", "chapipo", "chapichapo"]
    return R[randint(0,len(R)-1)]
def blague_ping(content, index):
    return "pong !"
def blague_hein(content, index):
    return "deux"


# Cherche le pattern dans message et applique func quand il est trouvé
def blague_chercher_faire(pattern, func, message):
    R = []
    index = message.find(pattern)
    while index != -1:
        R.append(func(message, index))
        index = message.find(pattern, index+1)
    return R

# Envoie les messages de la liste
async def send_msg(MSG, send_func):
    for m in MSG:
        if m != "":
            await send_func(m)

# Applique les blagues au message
async def blague(content, send_func):
    BLAGUES = [("di", blague_di), ("cri", blague_cri),
               ("quoi", blague_quoi), ("chapiro", blague_chapiro),
               ("comment", blague_comment), ("ping", blague_ping),
               ("hein", blague_hein)]
    for (pattern, func) in BLAGUES:
        await send_msg(blague_chercher_faire(pattern, func, content), send_func)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_traite = message.content.lower()
    if message_traite.startswith('bonjour'):
            await message.channel.send('Bonsoir ! <3')

    
    await blague(message_traite, message.channel.send)


client.run('')
