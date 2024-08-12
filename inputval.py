ok = false 
while ok is False:
    try:    
        age = int(age)
        ok = True
    except:
        n += 1
        print(age+" isn't a number, you embacile! This is the "+ ordinal(n) +" time I've asked you, now try again!")
        age = input ("How old are you, REALLY? ")