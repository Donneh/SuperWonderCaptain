def comichint(superheld):
    if superheld["comics"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["comics"]["returned"])

        return superheld["comics"]["items"][randomnumber]

    return False


def beschrijvinghint(superheld):
    if superheld["description"]:
        return superheld["description"]

    return False


def serieshint(superheld):
    if superheld["series"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["series"]["returned"])

        return superheld["series"]["items"][randomnumber]

    return False


def eventshint(superheld):
    if superheld["events"]["returned"] > 0:
        randomnumber = random.randrange(0, superheld["events"]["returned"])

        return superheld["events"]["items"][randomnumber]

    return False

