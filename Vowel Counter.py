def vowelcounter():

    original = input("Enter a word: ")
    counted = (original.count("a") + original.count("e") + original.count("i") + original.count("o") + original.count("u"))
    print(original + " has " + str(counted) + " vowel(s)!")

    vowelcounter()
vowelcounter()
