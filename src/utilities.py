def parse_userid(userid):
    print(userid)
    parsedID = userid.replace("<@", "")
    print(parsedID)
    parsedID = parsedID.replace(">","")
    print(parsedID)
    parsedID = int(parsedID)
    print(parsedID)
    return parsedID
