print("Welcome to Grade Generator!")
print()

name = input("What is your name? ")
test = input("Give a name of any test that you have taken: ")
maxScore = int(input("What was the maximum score on the test? "))
score = float(input("What was your score on the test? "))
percent = (score / maxScore) * 100
percent = round(percent, 2)
print()
print("You got " + str(percent) + "% on your " + test + " test!")

if percent >= 90:
  print("Great job!! You got an \033[34mA+!!!")
elif percent >= 80:
  print("Awesome! You got an A!!")
elif percent >= 70:
  print("Good! You got a B.")
elif percent >= 60:
  print("Fine. You got a \033[33mC\033[0m. Gotta work harder!")
elif percent >= 50:
  print("You got a \033[31mD\033[0m. Try harder next time!!!")
else:
  print("Oh, You got an \033[31mU\033[0m. You got lots of work to do!")