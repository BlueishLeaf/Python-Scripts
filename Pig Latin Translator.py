def piglatin ():
    
    original=input("Enter the word you want translated: ")
    print("Okay, converting "+original+" into pig latin...")
    translated=original[1:]+original[0]+"ay"
    print(original+" in pig latin is "+translated)

    piglatin()
piglatin()
