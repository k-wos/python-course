contacts = {
    "Natalia": "natalia@exapmple.com",
    "Adam": 30,
    "Ania": "ania@exapmple.com",
}

contacts["Rafał"] = "rafał@example.com"

print(contacts["Natalia"])
print(type(contacts))
print(len(contacts))

print(contacts.keys())
print(contacts.values())

for key in contacts:
    print(key + " " + str(contacts[key]))
    
for key, value in contacts.items():
    print(key, " ", value)