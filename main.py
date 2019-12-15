import os
import discord
import asyncio
from discord.utils import get
from datetime import datetime as dt
from datetime import timedelta as td
from datetime import timezone as tz


TOKEN = os.environ["TOKEN"]

client = discord.Client()  

#await asyncio.sleep(10)

@client.event  
async def on_member_join(member): 
    await asyncio.sleep(2)
    channel = client.get_channel(594745608674476041) #welcome
    bot_message = await channel.send("テスト\naho ok? plz push any button")
    #aho yes
    await bot_message.add_reaction(":Yes:615111453996875776")#client.get_emoji(614753778888867870)
    #await bot_message.add_reaction(client.get_emoji(612981509250351134))#client.get_emoji(612981509250351134)
    #aho no
    await bot_message.add_reaction(":No:615111447411818506")#client.get_emoji(614753822530600960)
    #await bot_message.add_reaction(client.get_emoji(612981535917867037))#client.get_emoji(612981535917867037)

    @client.event
    async def on_raw_reaction_add(payload):
        if payload.message_id == bot_message.id and bot_message.author.id != payload.user_id:
            guild = client.get_guild(payload.guild_id)
            channel = client.get_channel(payload.channel_id)
            usr = guild.get_member(payload.user_id) #role =  member.roles[1]
            temp_content = bot_message.content

            if member == usr: 
                print(str(payload.emoji.name))
                if str(payload.emoji.name) == "Yes":
                    role = guild.get_role(612974503953301535)
                     #aho ok 612974503953301535 ng 612986991289827328
                elif str(payload.emoji.name) == "No":
                    role = guild.get_role(612986991289827328)

                await usr.add_roles(role)
                await bot_message.edit(content="ご協力ありがとうございます")
                await asyncio.sleep(10)
                await bot_message.delete()

#↓時刻bot by hibit

def what(datetime):
    if datetime.hour <=4:
        return("go to bed!")
    elif datetime.hour <=6:
        return("early morning!")
    elif datetime.hour <=11:
        return("morning!")
    elif datetime.hour <=15:
        return("afternoon!") 
    elif datetime.hour <=17:
        return("evening!")
    else:
        return("night!")

def zone_decide(utc):
    summer = td(hours = 0)
    if utc.month > 3 and utc.month < 11:
        summer = td(hours = -1)
    jst = utc + td(hours = 9)
    cet = utc + td(hours = 1) + summer
    est = utc + td(hours = -5) + summer
    pst = utc + td(hours = -8) + summer
    return [jst,cet,est,pst]

@client.event
async def on_message(message):
    if message.content == '/now':
        utc = dt.now(tz.utc)
        area = ['Japan(JST) is','Europe(CET) is','East America(EST) is','West America(PST) is']
        timezones = zone_decide(utc)
        content = "Let me show the current time\n"
        for a,t in zip(area,timezones):
            content = content + a + t.strftime("%Y/%m/%d %H:%M") + "!　" + what(t) + "\n"
        await message.channel.send(content)

    if message.content.startswith('/world'):
        
        d = message.content.split()

        if len(d)<6:
            await message.channel.send(" please command like /world 2019 12 31 23 55 pst")

        for i in range(1,6):
            d[i] = int(d[i])

        utc = dt(d[1],d[2],d[3],d[4],d[5])
        suc = 1

        if len(d) == 6: 
            utc = utc - td(hours = 9)
        elif len(d) == 7:
            if d[6] == 'jst':
                utc = utc - td(hours = 9)
            elif d[6] == 'cet':
                utc = utc - td(hours = 1)
            elif d[6] == 'est':
                utc = utc - td(hours = -4)
            elif d[6] == 'pst':
                utc = utc - td(hours = -7)
            else:
                await message.channel.send("wrong time zone!")
                suc = 0
        else:
            await message.channel.send("wrong input!")
            suc = 0

        if suc:    
            area = ['Japan(JST) is','Europe(CET) is','East America(EST) is','West America(PST) is']
            timezones = zone_decide(utc)
            content = 'Let me convert the input datetime'
            for a,t in zip(area,timezones):
                content = content + a + t.strftime("%Y/%m/%d %H:%M") + "!　" + what(t) + "\n"
            await message.channel.send(content)
#↑時刻bot by hibit


print("running bot...")

client.run(TOKEN)
