experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("warunki spełnione")
    else:
        print ("zle warunki umowy")
else:
    print("nie spełnia wymagań")