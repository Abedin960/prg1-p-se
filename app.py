påse = True 
inventory = []
print("Välkomen till din inverntory!") 

while påse:
    print("Visa innehållet [V]")
    print("spara i påsen [S]")
    print("Ta bort sak [T]")
    print("Sortera påsen [O]")
    print("Avsluta programet [Q]")
    choice = input("Välj:")

    if choice.lower() == "v":
       for thing in inventory:
           print(thing)
    
    elif choice.lower() == "s":
        inventory.append(input("skriv vad ud vill spara:"))  

    elif choice.lower() == "t":
        sak = input("Skriv vad du vill ta bort: ")
        if sak in inventory: 
            inventory.remove(sak)
            print(sak, "har tagits bort från påsen.") 
        else: 
            print("Den saken finns inte i påsen.")

    elif choice.lower() == "o": 
        inventory.sort() 
        print("Påsen har sorterats.") 

    elif choice.lower() == "q":  
        påse = False 

    elif choice.lower() == "f":
        query = input(" vad vill du söka efter?: ")
        if query.lower() in påse:
            print(f"Hittade: {query} i påsen.")
    else:
        print("Felaktig kommando, Försök igen.")

        