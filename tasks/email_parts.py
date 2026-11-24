def getEmailParts(email):
    monkeyIndex = email.find("@")
    if monkeyIndex == -1: return None
    
    dotIndex = email.rfind(".")
    if dotIndex == -1: return None
    
    user = email[0:monkeyIndex]
    domain = email[monkeyIndex + 1:dotIndex]
    domainExt = email[dotIndex +1 : len(email)]
    
    return {
        "user": user,
        "domainName": domain,
        "domainExt": domainExt
    }
    
print(getEmailParts("ola@domena.com"))