import random

print("Lets play guess the number game!")
max = 1000000
print("I am picking a number between 1 and {}".format(max))
print()

number = random.randint(1, max)
print("Lets begin the guessing now!")
print()
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