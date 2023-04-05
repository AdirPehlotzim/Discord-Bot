import discord
from discord.ext import commands
import random


# classes

def has_admin_rules(admin_roles, message):
    for role in message.guild.roles:
        if role.permissions.administrator:
            admin_roles.append(role.name)
    has_admin_role = False
    for role in message.author.roles:
        if role.name in admin_roles:
            has_admin_role = True
            break
    return has_admin_role


def has_swear(swear_list, message):
    contains_swear_word = False
    for word in message.split():
        if word.lower() in swear_list:
            contains_swear_word = True
            break
    return contains_swear_word


class MessageDefiner:
    def __init__(self, message):
        self.message = message
        helper = message.split()
        self.second_word = helper[1]
        self.third_word = helper[2]





# main

intents = discord.Intents.all()
token = 'MTA4OTkyNDUyNzYwNzI3MTYyNg.GNVhWb.CORXZlVFU3yQUi-L4YFoBfSqLZ6-3vtfoqcLRI'
bot = commands.Bot(command_prefix='.', intents=intents)


def exit_handler():
    @bot.event
    async def not_on_ready():
        channel = bot.get_channel(1074836321765437460)
        await channel.send('Iam Offline @here')


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    channel = bot.get_channel(1074836321765437460)
    await channel.send('Iam Online ')


@bot.event
async def on_message(message):
    klalot = ["nigger", "n1gger", "sharmota", "niggers", "Hello liam"]
    sean = ["seaning", "sean", "sean2008"]
    fortnite23 = ["fortnite23"]
    adirelad = ["hatzil", "adirelad"]
    adirelad_images = ["https://cdn.discordapp.com/attachments/853208275268534273/1091092842807558225/1_3.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092843046645910/1_1.jpg",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092843520594100/1_1.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092842060976178/1_2.jpg",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092842472018130/1_2.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092822301618307/1_30.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092822553264330/1_31.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092822783954974/1_32.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092821416620133/1_8.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092821714403338/1_9.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092821995425853/1_10.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092820485484694/1_5.jpg",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092820821016596/1_5.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092820196069488/1_4.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092738449092749/1_25.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092735584374804/1_27.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092690755665940/1_76.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092691166691398/1_77.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092689715462174/1_64.png",
                       "https://cdn.discordapp.com/attachments/853208275268534273/1091092508097921136/1gt56vwg0g251.jpg"]
    fortnite23_images = ["https://cdn.discordapp.com/attachments/1030034211110916137/1048970884918038598/733s4q.png",
                         "https://cdn.discordapp.com/attachments/1030034211110916137/1048592711873220700/image.png",
                         "https://cdn.discordapp.com/attachments/1030034211110916137/1048592662795649135/image.png",
                         "https://cdn.discordapp.com/attachments/1030034211110916137/1048592644705615904/730brm.png",
                         "https://media.discordapp.net/attachments/1041058684639391787/1048566522433523732/730bhm.gif",
                         "https://media.discordapp.net/attachments/748290499210903606/1048566868622975096/730bky.gif",
                         "https://media.discordapp.net/attachments/748290499210903606/1048567425160978503/730bp7.gif"]
    sean_images = [
        "https://cdn.discordapp.com/attachments/1074836321765437460/1091085685387182160/WhatsApp_Image_2023-03-14_at_18.09.33.jpeg",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091088537014784072/5e95161aeeafb70d.jpeg",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091088537274822716/6c5f872fc515f32d.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091088537513885839/84446897110977e3.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091088537790730271/6.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091088538080129085/2.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091088538302414848/6753dca5394559bf.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091089850855325746/e69465fb-6bcf-4119-bed8-08409f6801fc.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091090096280846426/image.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091090248529879111/image.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091090270239592480/image.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091090287067144293/image.png",
        "https://cdn.discordapp.com/attachments/853208275268534273/1091090304372838400/image.png"]
    admin_roles = []
    for role in message.guild.roles:
        if role.permissions.administrator:
            admin_roles.append(role.name)

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    user_message = user_message.lower()
    channel = str(message.channel.name)
    for_commands = user_message.lower()
    print(f'{username}: {user_message}: {channel})')

    if message.author == bot.user:
        return

    if message.channel.name == 'bot_commands':
        if user_message.lower() == "hello":
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!help':
            if has_admin_rules(admin_roles, message):
                await message.channel.send(
                    f'Hello {username} here are some commands that you can use \n 1.write "seaning", "sean", "sean2008", to get a random number of sean \n 2. write "fortnite23", to get a random photo of fortnite season 23 \n 3. write "hatzil","adirelad", to get a random photo of adirelad  ')
                return
            else:
                await message.channel.send(f'fuck you')
                return
        elif has_swear(klalot, user_message):
            await message.channel.send(f'fuck you')
            return

        elif has_swear(fortnite23, user_message):
            random_number = random.randint(1, len(fortnite23_images))
            helper = fortnite23_images[random_number]
            await message.channel.send(f'{helper}')
            return
        elif has_swear(adirelad, user_message):
            random_number = random.randint(1, len(adirelad_images))
            helper = adirelad_images[random_number]
            await message.channel.send(f'{helper}')
            return

        elif has_swear(sean, user_message):
            random_number = random.randint(1, len(sean_images))
            helper = sean_images[random_number]
            await message.channel.send(f'{helper}')
            return


bot.run(token)
