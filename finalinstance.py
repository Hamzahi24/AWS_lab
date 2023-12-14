'''Import of the class libraries to interact with discord, import the token file, interact with operating system and randomly generate
something, folder structure importing the token from dotenv'''

import discord 
import os 
import random 
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

load_dotenv()

 #Assigning variables for client from the discord class, Client subclass.
 #Insert the token for OAuth2.
 
client = discord.Client() 
token = os.getenv('TOKEN')

'''Event driven programming initiating the function when the client event connects to discord. Formatting of the string
into the argument parameter with the brackets. Creating an output to the terminal window formating a string'''

@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))

'''Event driven by the client passing information needed to process. Creating three objects first outputting a message
in a string. Convert the objects with the string function, data type, indexing and splitting the string because of #.'''

@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
    
    #Output, format(f) with brackets.
    print(f'Message {user_message} by {username} on {channel}') 
    
    #Client user is the bot if the user is the bot.
    if message.author == client.user: 
        return
    
    '''If condition for channel if in random it'll run all condition statements that checks the string indexes and lower case values
    of several different strings'''
    try:                                             #Error handling when bot messages fails to send.
        if channel == "random": 
            if user_message.lower() == "hello" or user_message.lower() == "hi": 
                await message.channel.send(f'Hello {username}') #Format string
                return #Returning values passed into the function
            
            #Nested if condition to output 'hello' if user inputs 'hello world'.
            elif user_message.lower() == "hello world":
                try:                                      #Error handling when bot messages fails to send.      
                    await message.channel.send(f'hello') 
                except discord.errors.HTTPException as err:     #The output if an error occurs.
                    print(f'Message wasn\'t sent. Try again: {err}')

            #Nested if condition to output my ec2 server data if user inputs 'tell me about my server!'.
            elif user_message.lower() == "tell me about my server!": 
                try:                                    #Error handling when bot messages fails to send.
                    await message.channel.send(f'Your ec2 server data:\nRegion: {ec2_metadata.region}\nIP Address: {ec2_metadata.public_ipv4}\nZone: {ec2_metadata.availability_zone}\nServer Instance: {ec2_metadata.instance_type}')
                except discord.errors.HTTPException as err:         #The output if an error occurs.
                    print(f'Message wasn\'t sent. Try again: {err}')

            #Nested if condition to output 'Bye' if user inputs 'bye'.
            elif user_message.lower() == "bye": 
                try:                                                #Error handling when bot messages fails to send.
                    await message.channel.send(f'Bye {username}')
                except discord.errors.HTTPException as err:         #The output if an error occurs.
                    print(f'Message wasn\'t sent. Try again: {err}')

            else:
                await message.channel.send(
                    f"I'm sorry, the command '{user_message}' is not a valid command."
                )
    except Exception as error:          #The output if an error occurs.

        print(f'The following error occured: {error}')
        
 
#Start execution by passing the token object.
client.run(token)