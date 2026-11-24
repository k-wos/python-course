multiLine = """Hello
CO tam
"""
print(multiLine)

print("test".center(10, "*"))

print("Ala ma kota".find("ma"))
print("Hello" * 3)

string = "Hello World!"
print(string[0])
print(string[0:5])

print ("Hello" in string)
print ("Hello" not in string)

print("ala".capitalize())
print("Ola ma kota, Ola ma psa.".count("Ola"))

print(string.startswith("Hello"))
print(string.endswith("World!"))

print(string.find("World"))

print("ala".capitalize())
print("Ola ma kota, Ola ma psa".count("Ola"))

print("Hello".center(20,"_"))

print("Hello World".startswith("Hello"))

print(string.find("Ola"))
print("Ola ma psa, Ola ma kota".rfind("Ola"))

print("232321".isalnum())
print("23232.1".isalnum())
print("23232.1".isalpha())

print("-|".join(["Ala", "Ola", "Adam"]))

print("Hello World".lower())
print("Hello World".upper())
print("Hello World".swapcase())

print("         \n \t Hello world \n\n".lstrip())
print("         \n \t Hello world \n\n".rstrip())
print("         \n \t Hello world \n\n".strip())

print("Ola ma psa, Ola ma kota".replace("Ola", "Ala"))


print("My name is {myName}, I'm from {country}".format(myName = "Kacper", country = "Poland"))