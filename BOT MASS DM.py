import discord
from discord.ext import commands
import random
from discord import Permissions
import os
import colorama
from colorama import Fore, Style
import asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from colorama import Fore, init 
import requests
import os 
import random

token = "BOT TOKEN HERE"

JANKY = commands.Bot(command_prefix='.')

client = commands.Bot(command_prefix='!')

JANKY.remove_command('help')

@JANKY.event
async def on_ready():
    activity = discord.Game(name="MADE BY JANKY", type=3)
    await JANKY.change_presence(status=discord.Status.idle, activity=activity)
    
@JANKY.event
async def on_connect():
    print(f'''{Fore.RED}
    
 ________  ________  _________                         
|\   __  \|\   __  \|\___   ___\                       
\ \  \|\ /\ \  \|\  \|___ \  \_|                       
 \ \   __  \ \  \\\  \   \ \  \                        
  \ \  \|\  \ \  \\\  \   \ \  \                       
   \ \_______\ \_______\   \ \__\                      
    \|_______|\|_______|    \|__|                      
                                                       
                                                       
                                                       
 _____ ______   ________  ________   ________          
|\   _ \  _   \|\   __  \|\   ____\ |\   ____\         
\ \  \\\__\ \  \ \  \|\  \ \  \___|_\ \  \___|_        
 \ \  \\|__| \  \ \   __  \ \_____  \\ \_____  \       
  \ \  \    \ \  \ \  \ \  \|____|\  \\|____|\  \      
   \ \__\    \ \__\ \__\ \__\____\_\  \ ____\_\  \     
    \|__|     \|__|\|__|\|__|\_________\\_________\    
                            \|_________\|_________|    
                                                       
                                                       
 ________  _____ ______                                
|\   ___ \|\   _ \  _   \                              
\ \  \_|\ \ \  \\\__\ \  \                             
 \ \  \ \\ \ \  \\|__| \  \                            
  \ \  \_\\ \ \  \    \ \  \                           
   \ \_______\ \__\    \ \__\                          
    \|_______|\|__|     \|__|                          
                                                       
                                                                                                                      
            {Fore.WHITE}[!] Made By Janky
          {Fore.WHITE}__________________________    
            {Fore.WHITE}
            {Fore.WHITE}[x] PLEASE
            {Fore.WHITE}[x] READ
            {Fore.WHITE}[x] THE
            {Fore.WHITE}[x] READ
            {Fore.WHITE}[x] ME
            {Fore.WHITE}[x] FILE
                                                                                               
                                                                               ''')

@JANKY.command()
async def massdm(ctx, *, dmall):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(dmall)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Mass DM")


try:
  JANKY.run(token)
except:
  JANKY.run(token, bot = False)
