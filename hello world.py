from Ordinal import ordinal

print("******************")

name = input ("What is your name? ")

print("Hello, " + name + "! Welcome to the simulation")

age = input ("How old are you? ")
ok = False
n = 1

while ok is False:
    try:    
        age = int(age)
        ok = True
    except:
        n += 1
        print(age+" isn't a number, you embacile! This is the "+ ordinal(n) +" time I've asked you, now try again!")
        age = input ("How old are you, REALLY? ")

if int(age) >= 18: 
    print("Congratulations, you may enter")
    print("******************************")

if int(age) <= 17: 
    print("Apologies, you are but a wee lad, now scuttle back to your mum's teet")
    print("*********************************************************************")