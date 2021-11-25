def parse_userid(userid):
    parsedID = int(userid.replace("<@!", "").replace(">", ""))
    return parsedID