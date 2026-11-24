def getUserInformation(name, surname, job):
        name = name.upper().strip()
        surname = surname.upper().strip()
        job = job.lower().strip()
        
        text = "imię: " + name + ", nazwisko: " + surname + ", zawód: " + job
        return text
    
    
user1 = getUserInformation("Ania", "Kowalska", "Programistka")
user2 = getUserInformation("Daniel", "Lis", "Administrator")

print(user1)
print(user2)