# referee-discord-bot

## Config Instructions

Config file is provided in src/config.txt with default messages and images for the bot,
you can add additional messages by adding key-value pairs or modify the current ones as you want,
if there's more than one entry of a key-value it will select a random one each time an action is called.  
<br>
To execute the bot a Discord bot token is needed, place the token in src/key.txt  
You can get one in [Discord's developer portal](https://discord.com/developers)  
You can also invite my instance of the bot to your discord server with this [link.](https://discord.com/api/oauth2/authorize?client_id=815975462412222464&permissions=8&scope=bot)

## Start the bot

Install the requirements and run the main from the root folder (python3 src/main.py).

### Run the main

Use the Makefile provided or run:

#### Linux

>python3 src/main.py

#### Windows

>python src/main.py

After executing the main you will see an "Online" message when the bot is ready.  
The database will be automatically created in the root folder.

