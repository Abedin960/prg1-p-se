påse = True 
inventory = []
print("Välkomen till din inverntory!") 

while påse:
    print("Visa innehållet [V]")
    print("spara i påsen [S]")
    print("Avsluta programet [Q]")
    choice = input("Välj:")
   
    if choice.lower () == "v":
       for thing in inventory:
           print(thing)
    
    elif choice.lower() == "s":
        inventory.append(input)("skriv vad ud vill spara:")

    elif choice.lower()== "q":
        påse = False
    
    else:
        print("Felaktig kommando, Försök igen.")
        