from mimetypes import init
import re
from turtle import color
from unicodedata import name
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import random
import time

load_dotenv(dotenv_path="config")


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        
    async def on_ready(self):
        print(f"{self.user.display_name} has connected to Discord!")

    async def on_message(self,message):
        print(message.content)
        fichier = open("log.txt", "a")
        fichier.write(str(message.author) + " at " + str(message.created_at) + " : " + message.content + "\n")
        fichier.close() 

        if message.content.lower() == "ping":
            await message.channel.send("pong")

        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()

        if message.content.startswith("!help"):
            await message.channel.send("Entrer : !del et un nombre pour supprimer un nombre de message\n!help pour afficher l'aide")




if __name__ == "__main__":
    #instance de monBot
    monBot=MyBot()
    #lancement de mon instance
    monBot.run(os.getenv("TOKEN"))
