from getpass import getpass as getpass

print("Lets play guess the number game!")
print()

max = 10000
number = -1
print("Player 1:")
while True:
  str = "Pick a number between 0 and {} : ".format(max)
  number = int(getpass(str))
  if number<0 or number>max:
    print("Number not within range. Try again!")
    continue
  else:
    break

print()
print("Player 2:")
print("Lets begin the guessing now!")

attempts = 0
while True:
  attempts += 1
  guess = int(input("Enter your guess: "))
  if guess < 0 or guess > max:
    print("Invalid guess!")
    exit()
  elif guess < number:
    print("Too low!")
  elif guess > number:
    print("Too high!")
  else:
    print("You got it!")
    print("You guessed in {} attempts".format(attempts))
    break