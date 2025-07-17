# Palindrome Checker:
# Write a program that repeatedly asks the user to enter a word.
# Use a while loop to continue prompting until the user enters "exit".
#  For each word entered (before "exit"), 
#  use an if-else statement to determine if the word is a palindrome (reads the same forwards and backwards, e.g.,
#  "madam", "level"). Print whether the word is a palindrome or not. 
#  (Hint: You might need string slicing or a loop to reverse the string for comparison).


# while True:
#     word = input("Enter a word: ")
#     if word.lower() == "exit":
#         print("Exiting the program.")
#         break  
#     if word == word[::-1]:
#         print(f"'{word}' is a palindrome.")
#     else:
#         print(f"'{word}' is not a palindrome.")

# output:
# Enter a word: 121 
# '121' is a palindrome.
# Enter a word: 131
# '131' is a palindrome.
# Enter a word: 33
# '33' is a palindrome.
# Enter a word: 22
# '22' is a palindrome.
# Enter a word: 12
# '12' is not a palindrome.
# Enter a word: 13
# '13' is not a palindrome.
# Enter a word: exit
# Exiting the program.

# Sentence Word Counter:
# Ask the user to enter sentences one by one. 
# Use a while loop to keep accepting input until the user types "STOP" (case-insensitive). 
# For each sentence entered, use an if-else statement to check if the sentence contains more than 5 words. 
# Print the sentence and indicate if it's "Long sentence!" or "Short sentence!".
#  (Hint: You can split the sentence into words using split() and then check the length of the resulting list).


# while True:
#     sentence = input("Enter a sentence: ")
#     if sentence.strip().lower() == "stop":
#         print("Program stopped.")
#         break
#     words = sentence.split()  
#     if len(words) > 5:
#         print(f'"{sentence}" → Long sentence!')
#     else:
#         print(f'"{sentence}" → Short sentence!')
# output:
# Enter a sentence: dheeraj
# "dheeraj" → Short sentence!
# Enter a sentence: dheeraj kumar sain 
# "dheeraj kumar sain " → Short sentence!
# Enter a sentence: my name is dheeraj sain im frome jaipur rajstan im persuing bca in jaipur national university jaipur
# "my name is dheeraj sain im frome jaipur rajstan im persuing bca in jaipur national university jaipur" → Long sentence!
# Enter a sentence: stop
# Program stopped.


# Ask the user to type a string.
#  Use a while loop to process characters one by one (you can iterate using an index that increments). 
# Maintain counts for:

#     Uppercase letters

#     Lowercase letters

#     Digits

#  Special characters (anything else)
#  Use if-elif-else statements to categorize each character.
#  Stop the loop if you encounter the character '#'. Finally,
#  print the counts for each type of character.
