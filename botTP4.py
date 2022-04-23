from mimetypes import init
from turtle import color
from unicodedata import name
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

load_dotenv(dotenv_path="config")


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        self.log = LogToi()
        
    async def on_ready(self):
        print(f"{self.user.display_name} has connected to Discord!")
        self.log.logInfo(f"{self.user.display_name} has connected to Discord!")


    async def on_message(self,message):
        fichier = open("log.txt", "a")
        fichier.write(str(message.author) + " at " + str(message.created_at) + " : " + message.content + "\n")
        fichier.close() 

        self.log.sauvgarde(message.author,message.content)


        if message.content.lower() == "hello":
            await message.channel.send("Heyyy!!")

        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()

        if message.content.startswith("!help"):
            await message.channel.send("Entrer : !del et un nombre pour supprimer un nombre de message\n!help pour afficher l'aide")



class LogToi():
    def __init__(self):
        logging.basicConfig(filename='logging.log', format='%(filename)s: %(message)s', level=logging.DEBUG)

    def bug(self):
        logging.warning("Error!!")
    
    def logInfo(self,message):
        logging.info(str(message))
        print(str(message))

    def sauvgarde(self,author,message):
        logging.debug(str(author)+" : "+str(message))





if __name__ == "__main__":
    #instance de monBot
    monBot=MyBot()
    #lancement de mon instance
    monBot.run(os.getenv("TOKEN"))
