print("Welcome to multiplication table challenge!")
print()
number = int(input("Enter a number of your choice: "))
print()
score = 0
for i in range (1, 11):
  answer = int(input("{} x {} = ".format(number, i)))
  if answer == number * i:
    if i % 2 == 0:
      print("Great work!")
    else:
      print("Awesome!")
    score += 1
  else:
    print("Wrong!")
  print()
print("Your score is {}/10".format(score))
if score == 10:
  print("Wow! You are a genius!")
elif score > 7 and score < 10:
  print("You did well!")
elif score > 5 and score < 8:
  print("You did alright!")
elif score > 3 and score < 6:
  print("You could do better!")
elif score > 1 and score < 4:
  print("You need to practice more!")
else:
  print("You need to try again!")
