def cToF(celcius):
    fahrenheit = celcius * 9 / 5 + 32;
    print(celcius, "stopni Celsjusza to", fahrenheit, "stopni fahrenheita")
    return fahrenheit

def fToC(fahrenheit):
    celcius = (fahrenheit - 32) * 5 /9;
    print(celcius, "\xB0 fahrenheita to", fahrenheit, "stopni Celsjusza")
    return celcius

cToF(20)
fToC(86)

