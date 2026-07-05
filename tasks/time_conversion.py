def convertToSeconds(hours, minutes):
    return hours * 3600 + minutes * 60

def convertToHours(minutes):
    return minutes / 60


print(convertToHours(120))
print(convertToSeconds(3, 25))