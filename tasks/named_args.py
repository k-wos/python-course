def createUserProfile(firstName, lastName, age, city):
    userProfile = {
        "firstName" : firstName,
        "lastName" : lastName,
        "age": age,
        "city": city
    }
    
    return userProfile

firstName = "Karol"
lastName = "Kowalski"
age = 23
city = "Kraków"

userProfile = createUserProfile(firstName=firstName, lastName=lastName, age=age, city=city)

print("Imię", userProfile["firstName"])
print("Nazwisko", userProfile["lastName"])
print("Wiek", userProfile["age"])
print("Miasto", userProfile["city"])