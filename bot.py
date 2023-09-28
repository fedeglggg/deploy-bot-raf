import discord
import local_settings

starting_command = "/deploy"

actions_msg = {
    "_online":"Yes, I'm here and available to assist you. How can I help you today?",
}

def get_response(user_message: str) -> str:
    message = user_message.lower()
    index = message.find(starting_command) + len(starting_command)
    action = message[index:]

    if action in actions_msg:
        return actions_msg[action]

    return "I don't recognize that command, sorry."

async def send_message(message, user_message, is_private):
    try:
        response = get_response(user_message)
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
		
		# Solo escucha mensajes que empiezen con /e
		user_message = str(message.content)
		if not user_message.startswith(starting_command):
			return
        
		username = str(message.author)
		channel = str(message.channel)
		print(f"{username} said: '{user_message}' ({channel})")
		await send_message(message, user_message,  is_private=False)

	client.run(TOKEN)

	



