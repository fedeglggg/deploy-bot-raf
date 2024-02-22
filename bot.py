import random
import discord
import local_settings
from git_repo import get_deploy_report, get_status

starting_command = "/deploy"


def get_online(message):
    return "Yes, I'm here and available to assist you. How can I help you today?"


def get_daily_host(message):
    channel = message.channel
    members = [member for member in channel.members if not member.bot]
    random_member = random.choice(members)
    return random_member


actions_msg = {
    "online": get_online,
    "daily_host": get_daily_host,
    "report": get_deploy_report,
    "status": get_status,
}


def list_commands(commands_dict):
    commands = "I don't recognize that command, sorry." + \
        "\n" + "Here's the list of avalible commands:" + "\n"
    for key in commands_dict.keys():
        commands = commands + starting_command + " " + str(key) + "\n"

    return commands


def get_response(message, user_message: str) -> str:
    command = user_message.split()
    action = command[1] if len(command) >= 2 else None
    params = command[2:] if len(command) >= 3 else []

    if action in actions_msg:
        return actions_msg[action](message, *params)

    default_action = list_commands(actions_msg)

    return default_action


async def send_message(message, user_message, is_private):
    try:
        response = get_response(message, user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_bot():
    TOKEN = local_settings.LOCAL_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Previene la ejecucion de la respuesta si el autor del mensaje es el mismo bot
        if message.author == client.user:
            return

        # Solo escucha mensajes que empiecen con /deploy
        user_message = str(message.content)
        if not user_message.startswith(starting_command):
            return

        username = str(message.author)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message.startswith("/deploy"):
            await send_message(message, user_message,  is_private=False)

    client.run(TOKEN)
