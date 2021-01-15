import discord
import os
import requests
import json
from bs4 import BeautifulSoup

client = discord.Client()

def aqi(city,state,country):
    url = 'http://api.airvisual.com/v2/city?city='+city+'&state='+state+'&country='+country+'&key=ADD YOUR KEY HERE'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    data = json.loads(soup.decode('utf-8'))
    aqi = (data['data']['current']['pollution']['aqius'])
    return 'AQI of '+city+' is: '+str(aqi)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_id = message.author.id

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
    if message.content.startswith('$aqi help'):
        await message.channel.send('This is an Air Quality Index information bot\n use $aqi city state country \nto know about AQI of a region')
    if message.content.startswith('$aqi id'):
        await message.channel.send(user_id)

    if message.content.startswith('$aqi'):
        userMessage = message.content
        inp = str(userMessage[5:])
        ls = inp.split(' ')
        city = ls[0]
        state = ls[1]
        country = ls[2]
        output = aqi(city,state,country)
        await message.channel.send(output)
        return

client.run('ENTER YOUR TOKEN HERE')
