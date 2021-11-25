import os

def load_messages():
    error_warnings = []
    error_yellows = []
    error_reds = []
    error_expulsions = []
    error_generic = []
    msg_coin_winner = []
    msg_coin_loser = []
    msg_greeting = []

    with open(os.getcwd() + "/src/config.txt") as file:
        for line in file:
            line = line.split("=")
            for i in range(0, len(line)):
                line[i] = line[i].strip()

            if line[0] == "error_warning":
                error_warnings.append(line[1])

            elif line[0] == "error_yellow":
                error_yellows.append(line[1])

            elif line[0] == "error_red":
                error_reds.append(line[1])

            elif line[0] == "error_expulsion":
                error_expulsions.append(line[1])

            elif line[0] == "error_generic":
                error_generic.append(line[1])

            elif line[0] == "msg_greeting":
                msg_greeting.append(line[1])

            elif line[0] == "msg_coin_winner":
                msg_coin_winner.append(line[1])

            elif line[0] == "msg_coin_loser":
                msg_coin_loser.append(line[1])

        return [error_warnings, error_yellows, error_reds, error_expulsions, error_generic, msg_greeting,
                msg_coin_winner, msg_coin_loser]


def load_imgs():
    img_warnings = []
    img_yellows = []
    img_reds = []
    img_expulsions = []
    img_trapcard = []

    with open(os.getcwd() + "/src/config.txt") as file:
        for linea in file:
            linea = linea.split("=")
            for i in range(0, len(linea)):
                linea[i] = linea[i].strip()

            if linea[0] == "img_warning":
                img_warnings.append(linea[1])

            elif linea[0] == "img_yellow":
                img_yellows.append(linea[1])

            elif linea[0] == "img_red":
                img_reds.append(linea[1])

            elif linea[0] == "img_expulsion":
                img_expulsions.append(linea[1])

            elif linea[0] == "img_trapcard":
                img_trapcard.append(linea[1])

        return [img_warnings, img_yellows, img_reds, img_expulsions, img_trapcard]


def load_token():
    with open(os.getcwd() + "/src/key.txt") as f:
        line = f.readline()

    return line
