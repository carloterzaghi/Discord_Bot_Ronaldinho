from nextcord.ext import commands, tasks
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

db = firestore.client()

class Teste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name= "teste")
    async def send_teste(self, ctx):
        user = ctx.message.author.id
        await ctx.send("To funfa")

    @commands.command(name= "emoji")
    async def emoji(self, ctx):
        user = ctx.message.author.id
        msg = db.collection('Ronaldinho').document('mandar').get()
        print(msg.to_dict()['msg'])
        await ctx.send(":grinning:")
    

def setup(bot):
    bot.add_cog(Teste(bot))

Teste(commands.Cog).testando.start()