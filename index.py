bot_id = input('Bot id ')
guild_id = input('Guild id ')
redirect_uri = input('Redirect uri ')
url = f'https://discord.com/oauth2/authorize?&client_id={bot_id}&scope=bot&permissions=0&guild_id={guild_id}&response_type=code&redirect_uri={redirect_uri}'
print (f'Programm generated oauth url {url}')
