from Ordinal import ordinal

print("******************")

# Ask for user's name
name = input ("What is your name? ")

# Remove whitespace from str
name = name.strip()

# Greet the user
print("Hello, " + name + "! Welcome to the simulation")

#Below line used for testing
#print("Hello,",name,"! Welcome to the simulation")

# Ask for user's age
age = input ("How old are you? ")

# Create While Loop to prevent non-integer inputs from user's
# Inform the user how many times they've been asked for their age
# Ask for user's age again
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

# Grant access if user's age is 18 or greater
if int(age) >= 18: 
    print("Congratulations, you may enter")
    print("******************************")

# Deny access if user's age is 17 or lesser
if int(age) <= 17: 
    print("Apologies, you are but a wee lad, now scuttle back to whence you came")
    print("*********************************************************************")