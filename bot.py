# Criado por: @IgorFradi
# 03/08/2018
# Importa livrarias e arquivos necessários
print('Importando livrarias necessárias...')
import discord, asyncio, random, time
import config
from discord.ext import commands
print('Pronto!')
#

# Configurações do Bot
print('Carregando configurações...')
token = config.TOKEN                            # Setando a TOKEN
client = commands.Bot(command_prefix = '>')     # Setando o PREFIX
client.remove_command('help')                   # Removendo o HELP
print('Pronto!')
#

# Quando bot estiver pronto
print('Criando o client do bot...')
@client.event
async def on_ready():
    print('Pronto!')

    # Status do Bot - Informativos
    print('Alterando o status do bot...')
    await client.change_presence(
    game=discord.Game(name='Prefixo: > | By IgorFradi', type=1, url='https://www.twitch.tv/igorfradi'), status='streaming')
    print('Nome: %s' % client.user.name)
    print('ID: %s' % client.user.id)
    print('O bot tá pronto pra ser escravizado!')
    print('Invite Admin https://discordapp.com/oauth2/authorize?client_id=463804761138004019&scope=bot&permissions=8')
    print('Invite Não-Admin https://discordapp.com/oauth2/authorize/?permissions=1341643969&scope=bot&client_id=463804761138004019')
#

# Comandos #
#
# Regras
@client.command(pass_context=True)
async def regras(ctx):
    if ctx.message.author.server_permissions.manage_messages:
        embed = discord.Embed(title="Regras do Servidor", colour=discord.Colour(0xdd289b), description=" Para interagir no servidor, você precisa seguir algumas regras, ou poderá ser mutado, kickado e até mesmo banido!\n\n**As regras são essas:**")

        embed.set_thumbnail(url="https://i.imgur.com/RVPBBFM.png")
        embed.set_author(name="Max Palaro", url="https://www.youtube.com/MaxPalaro", icon_url="https://i.imgur.com/RVPBBFM.png")
        embed.set_footer(text="SadIgor bot © IgorFradi - 2018", icon_url="https://i.imgur.com/cqLMPao.png")

        embed.add_field(name="Tenha bom senso:", value="Qualquer discurso homofóbico, racista, misógino, xenofóbico, transfóbico é punido com permaban. Também tente não levantar discussões políticas ou militâncias desnecessárias.")
        embed.add_field(name="Não faça spam!", value="Spam é tudo que é chato: divulgação, flood/spam, pedir admin ou cargos, abusar de comandos, entre outros")
        embed.add_field(name="Respeite a Staff:", value="Sempre que alguém da staff te der um aviso, respeite. Vamos evitar confusão e punições desnecessárias!")
        embed.add_field(name="Não mencione atoa!", value="Não mencione ninguém sem motivo, principalmente cargos da Staff. As pessoas param o que estão fazendo para visualizar menções!")
        embed.add_field(name="Moderação Automática", value="Você será punido automaticamente ao enviar mensagens abusivas como: texto duplicado, CAPSLOCK EM EXCESSO, muitos emojis, menções demais, etc.")

        await client.say(content="**Seja bem vindo ao discord do MaxPalaro!**\n\n", embed=embed)
    else:
        await client.say(content="Ooops! Algo deu errado :s\nEntre em contato com um administrador! :D")
#

# Max Responde
@client.command(pass_context=True)
async def maxresponde(ctx):
    if ctx.message.author.server_permissions.manage_messages:
        embed = discord.Embed(title="Max Responde", colour=discord.Colour(0xdd289b), description="As mensagens que não seguirem as regras serão excluídas e poderão resultar em mute, kick e banimento!\n\n")

        embed.set_thumbnail(url="https://i.imgur.com/RVPBBFM.png")
        embed.set_author(name="Max Palaro", url="https://www.youtube.com/MaxPalaro", icon_url="https://i.imgur.com/RVPBBFM.png")
        embed.set_footer(text="SadIgor bot © @IgorFradi - 2018", icon_url="https://i.imgur.com/cqLMPao.png")

        embed.add_field(name="Mande coisas interessantes!", value="É mais provável que o Max te responda se tu mandar algo legal!")
        embed.add_field(name="É proibido pedir vídeo de X série", value="É proibido pedir vídeo de uma série em específica ou qualquer tipo de cobrança de vídeo/postagem.")
        embed.add_field(name="É proibido pedir salves", value="Não é permitido pedir salve ou afins em qualquer parte do servidor.")
        embed.add_field(name="Evite mensagem repetida!", value="É possível votar nas mensagens de outros inscritos. Tente não enviar perguntas repetidas!")

        await client.say(content="Participe da série **Max Responde!**\n\nLembre-se de seguir as regras abaixo e boa sorte!\n**O desrespeito às regras é punido com mute, kick ou até mesmo banimento.**", embed=embed)
    else:
        await client.say(content="Ooops! Algo deu errado :s\nEntre em contato com um administrador! :D")
#

# Divulgação
@client.command(pass_context=True)
async def divulgação(ctx):
    if ctx.message.author.server_permissions.manage_messages:
        embed = discord.Embed(title="Sala de Divulgação", colour=discord.Colour(0xdd289b), description="Essa é a sala de divulgação! Lembre-se de não quebrar as regras:")

        embed.set_thumbnail(url="https://i.imgur.com/RVPBBFM.png")
        embed.set_author(name="Max Palaro", url="https://www.youtube.com/MaxPalaro", icon_url="https://i.imgur.com/RVPBBFM.png")
        embed.set_footer(text="SadIgor bot © @IgorFradi - 2018", icon_url="https://i.imgur.com/cqLMPao.png")

        embed.add_field(name="Envie apenas uma mensagem a cada 2 dias", value="Você só pode enviar uma mensagem a cada dois dias. Isso ajuda a manter a sala livre de spam.")
        embed.add_field(name="Não enviar coisas repetidas", value="Apenas divulgue novos links. Para convites de outros grupos, só é permitido divulgar uma vez.")
        embed.add_field(name="Sem toxidade quando divulgar", value="Nada de follow-por-follow, like-por-like, implorar por atenção ou outras práticas tóxicas.")
        embed.add_field(name="Nada de NSFW!", value="Sem postar qualquer tipo de NSFW.")

        await client.say(content="**Bem vindo à sala de divulgação!**\nAqui você receberá notificações de vídeos e streams novas do MaxPalaro, além de poder também divulgar suas coisas.\n\n**Quebrar as regras acarretará em mutes longos (ou até mesmo kick e ban), leia com atenção:**", embed=embed)
    else:
        await client.say(content="Ooops! Algo deu errado :s\nEntre em contato com um administrador! :D")
#

# Ajuda
@client.command(pass_context=True)
async def ajuda(ctx):
    if ctx.message.author.server_permissions.manage_messages:
        embed = discord.Embed(title="Central de Ajuda", colour=discord.Colour(0xdd289b), description="Essa é a sala de ajuda!\n\nQualquer dúvida é só chamar xD")

        embed.set_thumbnail(url="https://i.imgur.com/RVPBBFM.png")
        embed.set_author(name="Max Palaro", url="https://www.youtube.com/MaxPalaro", icon_url="https://i.imgur.com/RVPBBFM.png")
        embed.set_footer(text="SadIgor bot © @IgorFradi - 2018", icon_url="https://i.imgur.com/cqLMPao.png")

        embed.add_field(name="Como acessar o servidor", value="É só se registrar no servidor! Basta utilizar o comando /registrar")
        embed.add_field(name="Fui punido injustamente!", value="O servidor possui moderação automática (!automod) e qualquer punição injusta pode ser contestada aqui.")
        embed.add_field(name="Quais são os comandos do server?", value="Basta perguntar neste chat qual bot você deseja utilizar e lhe informaremos os comandos ;)")
        embed.add_field(name="Como denunciar alguém?", value="Denuncias podem ser feitas diretamente para o Admin Líder: @IgorFradi#1084 (ID: 205817378808791041)")

        await client.say(embed=embed)
    else:
        await client.say(content="Ooops! Algo deu errado :s\nEntre em contato com um administrador! :D")
#

# Créditos
@client.command(pass_context=True)
async def créditos(ctx):
    embed = discord.Embed(title="Créditos", colour=discord.Colour(0xdd289b), description="Bem vindo à nova identidade visual do discord do MaxPalaro!\n\nEsse é um bot assistente criado especialmente para o servidor.")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/444804434078466078/474820098625110047/igor.png")
    embed.set_author(name="Igor Frade", url="https://www.twitch.tv/igorfradi", icon_url="https://i.imgur.com/cqLMPao.png")
    embed.set_footer(text="SadIgor bot © @IgorFradi - 2018", icon_url="https://i.imgur.com/cqLMPao.png")

    embed.add_field(name="Autor:", value="@IgorFradi", inline=True)
    embed.add_field(name="Linguagem:", value="Python / discord.py", inline=True)
    embed.add_field(name="Data:", value="03/08/2018", inline=True)
    embed.add_field(name="Contato:", value="igorlourenzofrade@gmail.com", inline=True)

    await client.say(content="", embed=embed)
#

# Criado por: @IgorFradi - 2018
#
# Loga o bot usando token externo
client.run(token)
