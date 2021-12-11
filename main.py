import discord
from discord.ext import commands
from discord_buttons_plugin import *
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or(""))
buttons = ButtonsClient(client)

@client.event
async def on_ready():
	print(f"Logged in as {client.user.name}")

@client.command()
async def invite(ctx):
	await buttons.send(
		content = None,
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Invite",
					url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
				)
			])
		]
	)

@buttons.click
async def RESELLER(ctx):
  await ctx.message.delete()
  embed1 = discord.Embed(title=f"WHAT YOU WANT TO RESELL", color=0xff7400,description=f"You must have Discord Server")
  embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    	embed = embed1,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "RESELL LIFETIME ",
					custom_id = "RESELL1",

				),

				Button(
					style = ButtonType().Primary,
					label = "RESELL 1 MONTH",
					custom_id = "RESELL2"
				),
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				)
			])
		]
	)
@buttons.click
async def PURCHASE(ctx):
  await ctx.message.delete()
  embed1 = discord.Embed(title=f"YOU CAN PURCHASE RIGHT NOW", color=0xff7400)
  embed1.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    	embed = embed1,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "LIFETIME X 100$",
					custom_id = "LIFETIME",

				),

				Button(
					style = ButtonType().Primary,
					label = "1 MONTH 30$",
					custom_id = "MONTH"
				),
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				)
			])
		]
	)
@buttons.click
async def QUESTIONS(ctx):
  await ctx.message.delete()
  embed2 = discord.Embed(title=f"QUESTIONS", color=0xff7400, description=f"HOW CAN I HELP YOU")
  embed2.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    embed = embed2,
		channel = ctx.channel.id,
    components = [
			ActionRow([
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				),
			])
		]
	)

@buttons.click
async def MONTH(ctx):
  await ctx.message.delete()
  embed4 = discord.Embed(title=f"MONTH", color=0xff7400, description=f"Our dedicated support team offers 24/7 support through our Forum, Discord and even TeamViewer.")
  embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    embed = embed4,
		channel = ctx.channel.id,
    components = [
			ActionRow([
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				),
			])
		]
	)

@buttons.click
async def RESELL1(ctx):
  await ctx.message.delete()
  embed4 = discord.Embed(title=f"LAST ENGINE RESELL LIFETIME KEYS ", color=0xff7400, description=f"With LAST ENGINE reseller program (updated for 2021), online shops and SPOOFER community owners can give their customers access to the same  that our members return month after month With hundreds of hours of development, our Spoofer  consistently outperform what our competitors offer. And while we've spent years updating our software to reach this point, you won't have to do the same.Expand the variety of titles you offer your customers by reselling our private Spoofer that deliver on the features your customers are looking for.")
  embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    embed = embed4,
		channel = ctx.channel.id,
    components = [
			ActionRow([
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				),
			])
		]
	)

@buttons.click
async def RESELL2(ctx):
  await ctx.message.delete()
  embed4 = discord.Embed(title=f"LAST ENGINE RESELL 1MONTH KEYS ", color=0xff7400, description=f"With LAST ENGINE reseller program (updated for 2021), online shops and SPOOFER community owners can give their customers access to the same  that our members return month after month With hundreds of hours of development, our Spoofer  consistently outperform what our competitors offer. And while we've spent years updating our software to reach this point, you won't have to do the same.Expand the variety of titles you offer your customers by reselling our private Spoofer that deliver on the features your customers are looking for.")
  embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    embed = embed4,
		channel = ctx.channel.id,
    components = [
			ActionRow([
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				),
			])
		]
	)

@buttons.click
async def LIFETIME(ctx):
  await ctx.message.delete()
  embed4 = discord.Embed(title=f"LIFETIME X 100$", color=0xff7400, description=f"Our dedicated support team offers 24/7 support through our Forum, Discord and even TeamViewer.")
  embed4.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    embed = embed4,
		channel = ctx.channel.id,
    components = [
			ActionRow([
				Button(

					style = ButtonType().Secondary,
					label = "Back",
					custom_id = "back",

				),
			])
		]
	)

@buttons.click
async def back(ctx):
  await ctx.message.delete()
  embed3 = discord.Embed(title=f"PLEASE CHOOSE WHAT YOU WANT", color=0xff7400,)
  embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
    content= None,
    embed = embed3,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Success,
					label = "PURCHASE",
					custom_id = "PURCHASE",

				),

				Button(
					style = ButtonType().Primary,
					label = "QUESTIONS",
					custom_id = "QUESTIONS"

				),
				Button(
					style = ButtonType().Danger,
					label = "RESELLER",
					custom_id = "RESELLER",
				)
			])
		]
	)

@client.command()
async def hello(ctx):
  embed3 = discord.Embed(title=f"PLEASE CHOOSE WHAT YOU WANT", color=0xff7400,)
  embed3.set_thumbnail(url='https://cdn.discordapp.com/attachments/909956529229275166/916632420172824576/LAST-ENGINE-LOGO.gif')  
  await buttons.send(
		content= None,
    embed = embed3,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Success,
					label = "PURCHASE",
					custom_id = "PURCHASE",

				),

				Button(
					style = ButtonType().Primary,
					label = "QUESTIONS",
					custom_id = "QUESTIONS"

				),
				Button(
					style = ButtonType().Danger,
					label = "RESELLER",
					custom_id = "RESELLER",
				)
			])
		]
	)

client.run(os.getenv("token"))