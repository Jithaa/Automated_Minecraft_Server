import discord
from subprocess import *
import threading
import time
from urllib.request import urlopen
import json
client = discord.Client()
import pexpect
a=[]
b=[]
def serv():
    Popen(["python3","tup.py"])
def pf():
    Popen(["python3","start.py"])
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$start server'):
        if len(a)==0:
            serv()
            a.append([f"{message.author} startred the server"])
            await message.channel.send(f'{message.author} the server is starting proceed to port forwarding!')
        else:
            if len(b)!=0:
                await message.channel.send(b[0])
            for i in range(len(a)):
                await message.channel.send(a[i])

        
    elif message.content.lower().startswith('$start pf'):
        if len(a)==1:
            pf()
            a.append(f"port forwarded by{message.author}")
            
            url = "http://127.0.0.1:4040/api/tunnels"
            response = urlopen(url)
            data_json = json.loads(response.read())
            ip=data_json['tunnels'][0]['public_url']
            b.append(f"server oniline @ {ip}")
            await message.channel.send(b[0])
        elif len(a)==0:
            await message.channel.send("Server is not started yet")
        else:
            for i in range(len(a)):
                await message.channel.send(a[i])
        
    elif message.content.lower().startswith('$stop'):
        import os;
        c=pexpect.spawn("sudo shutdown -r 1")
        c.expect('password')
        c.sendline('123456789')
        a.clear()
        await message.channel.send("Server Stopped Sucessfully")

client.run('ODY1Njc3MDk1NjA1NTAxOTcy.YPHenw.6ubELnXazbFDEXNqnqj2We-OZ3s')
