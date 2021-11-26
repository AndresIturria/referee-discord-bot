# referee-discord-bot

## Config Instructions
Config file is provided in src/config.txt with default messages and images for the bot, you can add or modify the values as you want.
To execute the bot a Discord bot token is needed, place the token in src/key.txt

## Start the bot
requirements.txt is provided, to install the dependencies first create a Virtual Enviroment.

### Virtual Enviroment (venv)
To create the Virtual Enviroment go to the root folder of the repository and run:
>venv venv

### Activate the venv
Go to venv/Scripts and execute the activate script (.bat for Windows, .sh for Linux).

### Install Dependencies
Go to the root folder of the project and run:
pip install -r requirements.txt

### Run the main
Use the Makefile provided or run:
#### Linux
>python3 src/main.py
#### Windows
>python src/main.py

After executing the main you will see an "Online" message when the bot is ready, the database will be created in the root if it doesn't exist.

