import discord
from subprocess import *
import threading
import pyautogui



client = discord.Client()
a=[]
def serv():
    Popen(["python3","tup.py"])
def pf():
    popen(["python3","start.py"])
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$start server'):
        if len(a)==0:
            threading.Thread(target=serv)
            a.append([f"{message.author} startred the server"])
            await message.channel.send(f'{message.author} the server is starting proceed to port forwarding!')
        else:
            for i in range(len(a)):
                await message.channel.send(a[i])

        
    elif message.content.lower().startswith('$start pf'):
        if len(a)==1:
            
            a.append(f"port forwarded by{message.author}")
            myScreenshot = pyautogui.screenshot()
            await message.channel.send("server online")
        elif len(a)==0:
            await message.channel.send("Server is not started yet")
        else:
            for i in range(len(a)):
                await message.channel.send(a[i])
        
    elif message.content.lower().startswith('$stop'):
        a.clear()
        await message.channel.send("Server Stopped Sucessfully")

client.run('ODY1Njc3MDk1NjA1NTAxOTcy.YPHenw.6ubELnXazbFDEXNqnqj2We-OZ3s')