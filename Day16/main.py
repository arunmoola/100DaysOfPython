print("Lets play guess the lyrics game!!")
print()
print("Here's a lyric with a missing word")
print()
print("The monster's running ____ inside of me")
print()
print("What is the missing word?")
guess = ""
attempts = 0;
while True:
  attempts += 1
  guess = input("Enter your guess: ")
  if guess == "wild":
    print ("You guessed it in {} attempts".format(attempts))
    print ("The monster's running {} inside of me".format(guess))
    break
  else:
    print("Sorry, that's an incorrect guess! Try again.")
print()
print("Thanks for playing!")