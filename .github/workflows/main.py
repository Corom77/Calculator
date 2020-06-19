import discord
import numpy as np
from discord.ext import commands
import math
import datetime



bot = commands.Bot(command_prefix='!')

jeton = ""#add here your bottoken

@bot.event
async def on_ready():
    print("The bot is ready!")
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game("activity"))

@bot.command()
async def aide(ctx):
    await ctx.send("LE bot est toujours en développement!Mais voici les commandes:!multiplication terme 1 terme2"
                   " !addition terme 1 terme2 !division terme 1 terme2 !soustraction terme 1 terme2 !sinus x !cosinus x !tangentente x"
                   "!arccosinus x!arcsinus x !arctangente x !racine x !aide_theoreme")
@bot.command()
async def aide_theoreme(ctx):
    await ctx.send("!pythagore !thales !millieu")

@bot.command()
async def pythagore(ctx):
    await ctx.send("Théorème de Pythagore — Dans un triangle rectangle, le carré de la longueur de l'hypoténuse est égal à la somme des carrés des longueurs des deux autres côtés.")

@bot.command()
async def thales(ctx):
    await ctx.send("Le théorème de Thalès est un théorème de géométrie qui affirme que, dans un plan, à partir d'un triangle, une droite parallèle à l'un des côtés définit avec les droites des deux autres côtés un nouveau triangle, semblable au premier (voir énoncé précis ci-dessous).")

@bot.command()
async def equivalence(ctx):
    await ctx.send("L'équivalence ricardienne associe impôt et déficit public : ce principe relève du comportement des contribuables aptes à associer dépenses publiques immédiates et taxes fiscales à venir, tout déficit public actuel équivalent à un report d'impôt ultérieur.")

@bot.command()
async def millieu():
    await ctx.send("Théorème — Si une droite passe par le milieu d'un des côtés d'un triangle et si elle est parallèle à un autre côté alors elle coupe le troisième côté en son milieu.")

@bot.command()
async def bonjour(ctx):
    await ctx.send("Salut l'ami!")

@bot.command()
async def multiplication(ctx,arg,arg1):
    result = int(arg) * int(arg1)
    phrase = "Le résulat de {}*{} est {} . ".format(str(arg),str(arg1),result)
    await ctx.send(phrase)

@bot.command()
async def addition(ctx,arg,arg1):
    result = int(arg)+int(arg1)
    phrase = "Le résulat de {}+{} est {} . ".format(str(arg),str(arg1),result)
    await ctx.send(phrase)

@bot.command()
async def division(ctx,arg,arg1):
    result = float(arg) / float(arg1)
    phrase = "Le résulat de {}/{} est {} . ".format(str(arg),str(arg1),result)
    await ctx.send(phrase)

@bot.command()
async def soustraction(ctx,arg,arg1):
    result = int(arg) - int(arg1)
    phrase = "Le résulat de {}-{} est {} . ".format(str(arg),str(arg1),result)
    await ctx.send(phrase)

@bot.command()
async def cosinus(ctx,arg):
    result = np.cos(float(arg))
    phrase = "Le cosinus de {} est {} .".format(str(arg),result)
    await ctx.send(phrase)

@bot.command()
async def sinus(ctx,arg):
    result = np.sin(float(arg))
    phrase = "Le sinus de {} est {} .".format(str(arg),result)
    await ctx.send(phrase)

@bot.command()
async def tangente(ctx,arg):
    result = np.tan(float(arg))
    phrase = "La tangente de {} est {} .".format(str(arg),str(result))
    await ctx.send(phrase)

@bot.command()
async def racine(ctx,arg):
    result = int(arg)**0.5
    phrase = "La racinne carré de {} est {} .".format(str(arg), str(result))
    await ctx.send(phrase)

@bot.command()
async def arctangente(ctx,arg):
    result = math.atan(float(arg))
    phrase = "L'arc tangente de {} est {} .".format(str(arg),str(result))
    await ctx.send(phrase)

@bot.command()
async def arcsinus(ctx,arg):
    result = math.asin(float(arg))
    phrase = "L'arc sinus de {} est {} .".format(str(arg),result)
    await ctx.send(phrase)

@bot.command()
async def arccosinus(ctx,arg):
    result = math.acos(float(arg))
    phrase = "L'arc cosinus de {} est {} .".format(str(arg),result)
    await ctx.send(phrase)

@bot.command()
async def time(ctx):
    date = datetime.datetime.now()
    phrase = "On est le {}/{}/{},il est actuellement {}:{} passé de {} secondes.".format(str(date.day), str(date.month),
                                                                                         str(date.year), str(date.hour),
                                                                                         str(date.minute),
                                                                                         str(date.second))
    await ctx.send(phrase)
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(jeton)
