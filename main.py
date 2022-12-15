from nextcord.ext import commands,tasks
import os 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import nextcord

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "zeebadata-d91ec",
    "private_key_id": "b65685ae72ded8aaf8b1817f29a812872f53684a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1lNZJ6SzdVQG9\nPULqpIpeuJd/9r2x/l8uahrVWt4lt/RPPwwKrF4XrU6lYQ7uDczdFs3qjH/F312T\njW3nWjro3/q/YYvbtEGZnq6cHoZtJOyyGB54tpkvTwczC+IJwURIuVwBSKCuO4b8\nTF4KwSd37SSG3n9xF2CdYSaFv8CjYcRJIz+JIIZfKdJgRUjv6CSne6A3YjLMWnbb\nSm7xkRISd7lBFWGdkXOgXpqGoHhQusG5SKeF4zo2VU5+oUH7uqy6UEWzW0q1cbLC\nd5ek0b9+3WrHtOmU0urzRz1XO5twJ20G0PPLR4urgt/S3GjxfdvwLPoEF8MjzVzY\nbZABMQPnAgMBAAECggEAFTawvEzODYOXYuzryu7zLXLCXFROwCM4KnuB7AgkKOLv\nW2zBsuOFUJ3SMNcAgAZDt1apMuw8JzlbvNfKjbtIY5l7OW2jgcTy3wgfXSThzpGA\nR6QytyaaCeFhNXD/dOVL3XUuTwYVo5VXxVUErZv4SPX/DPSkjelNw8UsU3beAhhA\n+rTitbMyTyQvqKSqZf8TxQPMOW4QFCNkOq5ZOBlwm+n1m9oz3d6yAm4sCgJ0Q4gN\n+95XxcRQ27ktj3ZDKSFAd/ycXrP9bGsNfquLUqiM9Cfu0TW1lZS8o4V9Uuhk9tTW\n6oGQi8ZFJDv16eh9HbbHv/72SO2DXDnUkP4zH5L+RQKBgQDjx9Lu9Q997lUyBYJa\nQZ21Q5uDOBtZxozsy7CZ9SNpE6WbRSa33rNTIl8JCRKOvVCGOFzBYMd638KIvlsW\nrBCq60lM9e9D6bP6gBsjx5nuJ/u0UuMyWefAoqrZ2pxSk1fg/B5Ys2LimhBiP1TY\nMxo3Oc6je4ewAYj38xCXapLmawKBgQDME8h38iyd+GmJ6IBCod7HuVn2IykKIgYI\ngxoLVmGzLnKS8sKwGI6FS+ORJmeRvaq++aFEFCdP3MhkzLwb/AtilIdnGbnLKp2T\nBWxiiaZecpY/1q83kCs0NATlmuQQ5oN9SP0qYxzioKHHwfVM5WDvswSSFgTfXhPA\nkM/vhKRfdQKBgQDOeaFkSLIdVkDWEhZiWF5sJHfAj8iDLa8rK0zPkl3h7xRMVnfN\nbsshDeQV3ap7x3JJ6Kd0B5VrdY/ywpLxT1HgjV2prLmR1zP1W9C+Mz3+mzHX+NbI\nGqUwgoPa7QaM99FOOVwMzbdSb5Nwa7YuMMyPyQ/eM6kAy7NsB2I/zzSQNwKBgQCb\nU19cc9WjsoPZdD3S+VMP3rJrFd3RmY3QAsDa6jdYYrzPvbeSwk4PhHBDdOCVW6/O\nxT8KCvDU5y0bE30FK7QapwPb5Ae2a8wdL56L7UrUThCvrB4Wg0Nu6zzi6R43AswH\nmnsePOuqTip0WNr0WQ2Lw0xySBITVI5iHZY2LlXRVQKBgA0v85RSkEuWtfB/eLCI\nKrXeDUWtB7zKe4M+/SO1ZYPjPwonWNT5J26UYEgPA6MoqmsExW5i2zW7aIxnonM6\neAoAlSyW8k7ruywQeoJeyrg5ScXOHoZjKuV7YufV4Zug1VpHSDJ4jnoidmTJ8q3F\nl6C/afC/8MrOuTsZ10Nsenh+\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-y5j9q@zeebadata-d91ec.iam.gserviceaccount.com",
    "client_id": "111104499525836044876",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-y5j9q%40zeebadata-d91ec.iam.gserviceaccount.com"
  })
firebase_admin.initialize_app(cred)
db = firestore.client()


bot = commands.Bot(command_prefix= 'r10')


@bot.event
async def on_ready():
    print(f"{bot.user.name} está online!")
    mandar.start()

# def load_cogs(bot):
#     for file in os.listdir("commands"):
#         if file.endswith(".py"):
#             cog = file[:-3]
#             bot.load_extension(f"commands.{cog}")

# load_cogs(bot)

@tasks.loop(seconds=3)
async def mandar():
        channel = bot.get_channel(951579040320462858)
        msg = db.collection('Ronaldinho').document('mandar').get()
        if msg.to_dict()['msg'] == 'test':
            pass
        else:
            embed = nextcord.Embed(
                title = "__Informações de Daily__",
                description = f"{msg.to_dict()['msg']}",
                color = 0x97CBFF
            )   
            await channel.send(embed = embed)
            db.collection('Ronaldinho').document('mandar').update({
                'msg' : 'test'
            })

with open("./.env") as f:
    _token = f.read().strip()


if __name__ == "__main__":
    bot.run(_token)
