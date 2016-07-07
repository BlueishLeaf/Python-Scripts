def palindrome():

     original = input("Enter a word: ")
     if len(original) < 3:
          print("Invalid!")
     else:
          original = original.lower()
          reverse = str(original[::-1])
          list1 = list(original)
          list2 = list(reverse)
          if list1 == list2:
               print(original.upper() + " is a palindrome!")
          else:
               print(original.upper() + " is not a palindrome")
               
     palindrome()
palindrome()
