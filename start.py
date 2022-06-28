import os
os.chdir("/")
os.chdir("/home/sjm/Documents/forge_server")#Server file location
k=os.system("./ngrok tcp -region=ap 25565")

