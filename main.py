import os
import discord
import asyncio
from discord.utils import get


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

print("running bot...")

client.run(TOKEN)