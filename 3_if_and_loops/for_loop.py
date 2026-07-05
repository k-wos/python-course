for v in [1,2,3,4]:
    print(v)
    
    
dictionaryData = {"Ania" : "ania@example.com", "Adam" : "adam@example.com"}

for key in dictionaryData:
    print(key)
    
for key in dictionaryData.keys():
    print(key)
    
for key in dictionaryData.keys():
    print(dictionaryData[key])
    
for key, value in dictionaryData.items():
    print(key + ":" + value)