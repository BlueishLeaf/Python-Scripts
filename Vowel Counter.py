def vowelcounter():

    original=input("Enter a word: ")
    vowels=["a", "e", "i", "o", "u"];
    list(original);
    print(len(set(vowels).intersection(original)))

    vowelcounter()

vowelcounter()
