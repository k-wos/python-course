def cleanText(text):
    text = text.replace("javascript", "*" * 10)
    return text
    
    
    
print(cleanText("Poznałem javascript"))