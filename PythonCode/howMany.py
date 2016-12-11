def howMany(aDict):
    total = 0
    values = aDict.values()
    for x in values:
        total+= len(x)
    return total
