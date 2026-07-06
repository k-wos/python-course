def info(email, country = "Polska", company = "Example Ltd"):
    user = {
        "email" : email,
        "country" : country,
        "company" : company
    }
    return user

print(info("ola@example.com"))