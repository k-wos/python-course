numbers = [1,2,3,4,5,6,7,8]

if 7 in numbers:
    print("7 w liście")
else:
    print("7 nie jest w liście")
    
animals = ("pies", "ryba", "jeleń")

if "kot" not in animals:
    print("kot nie jest w krotce")
else:
    print("kot w krotce")
    
user = {"name": "Jan", "age": 35}

if "name" in user:
    print("Klucz name jest w słowniku")
else:
    print("klucza nie ma ")