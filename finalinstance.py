import discord 
import os 
import random 
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

load_dotenv() 
  
client = discord.Client() 
token = os.getenv('TOKEN')

@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))

@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == client.user: 
        return
  
    if channel == "random": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hello {username}') 
            return
        elif user_message.lower() == "hello world": 
            await message.channel.send(f'hello') 
        elif user_message.lower() == "tell me about my server!": 
            await message.channel.send(f'Your ec2 server data:\nRegion: {ec2_metadata.region}\nIP Address: {ec2_metadata.public_ipv4}\nZone: {ec2_metadata.availability_zone}\nServer Instance: {ec2_metadata.instance_type}')
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Bye {username}')

 

client.run(token)