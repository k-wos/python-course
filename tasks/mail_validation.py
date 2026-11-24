def validateEmail(email):
    monkeyIndex = email.find("@")
    if monkeyIndex < 0: return False
    
    dotIndex = email.find(".")
    if dotIndex == -1: return False
    if monkeyIndex > dotIndex: return False
    
    
    return True
    



print(validateEmail("asia@example.com"))
print(validateEmail("karol@domena"))
print(validateEmail("user.com"))