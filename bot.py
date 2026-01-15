import discord
import requests
import json
import os



def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith("We"):
            await message.channel.send("Goated")
        
        if message.content.startswith("$hello"):
            await message.channel.send("Hello World!")

        if message.content.startswith("meme"):
            await message.channel.send(get_meme())

        if message.content.lower() == "blue":
            guild = message.guild
            member = message.author
            role_name = "Blue Team" 

            role = discord.utils.get(guild.roles, name=role_name)


            if not role:
                try:
                    role = await guild.create_role(name=role_name, color=discord.Color.blue())
                    await message.channel.send(f"Yessir brother is '{role_name}'!")
                except discord.Forbidden:
                    await message.channel.send("No permission gang")
                    return

            try:
                await member.add_roles(role)
                await message.channel.send(f"{member.mention} is Blue!")
            except discord.Forbidden:
                await message.channel.send("big L")

        


        if message.content.lower() == "red":
            guild = message.guild
            member = message.author
            role_name = "Red Team" 

            role = discord.utils.get(guild.roles, name=role_name)


            if not role:
                try:
                    role = await guild.create_role(name=role_name, color=discord.Color.red())
                    await message.channel.send(f"Yessir brother is '{role_name}'!")
                except discord.Forbidden:
                    await message.channel.send("No permission gang")
                    return

            try:
                await member.add_roles(role)
                await message.channel.send(f"{member.mention} is red!")
            except discord.Forbidden:
                await message.channel.send("big L")

    
    
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)

token = os.getenv("MTQ1MDk2Mjg1MTA3MzM2NDIwMA.GGhVGi.o5dUBYskqDjbBqdS_ymPFIWfLSyxFT1cSn4ZgM")
client.run(token)

