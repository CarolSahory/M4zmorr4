from twitchio.ext import commands
from datetime import datetime
import time
from os import system
system("title KUKORO - MAZMORRA")

# REEMPLAZAR POR TUS DATOS
Canales = [elsushipan]
Administradores = [elsushipan, tupadre171']
Comando = !CarolSahory
TokenTwitch = oauth:w6e6vzu78cyty48kheoanh0ik6blw5'

class Bot(commands.Bot):
    def __init__(self):         
        super().__init__(token = TokenTwitch, prefix = '_0n', initial_channels = Canales)

    async def event_ready(self):   
        print(f'\x1b[3;35m --> {self.nick.capitalize()}\x1b[3;32m conectado a {Canales}\x1b[0;m')  
        print(f'\x1b[3;35m --> Administradores: \x1b[3;37m{Administradores}\x1b[0;m')  
        print(f'\x1b[3;33m --> {Comando}\x1b[3;34m para invocarlo') 
        
    async def event_message(self, ctx):
        if ctx.echo:
            return
        Canal = (f'{ctx.channel}').replace('<Channel name: ','').replace('>','')
        Mensaje = f'{ctx.content}'
        if(Administradores.__contains__(ctx.author.name)):
            if(Mensaje.lower() == Comando.lower()):                             
                await ctx.channel.send('!KuKoRo')
                time.sleep(2)
                await ctx.channel.send('!GeTiNfO')
                now = datetime.now()                
                fechahora = now.strftime("%d/%m/%Y %H:%M:%S") 
                print(f'\x1b[3;36m --> [{fechahora}] Invocado por {ctx.author.name} en {Canal}\x1b[0;m')                            
bot = Bot()
bot.run()
