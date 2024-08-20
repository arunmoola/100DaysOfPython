def myPrint(text, color):
  if color == "red":
    print("\033[31m",text,"\033[0m", end="", sep="")
  elif color == "blue":
    print("\033[34m",text,"\033[0m", end="", sep="")
  elif color == "green":
    print("\033[32m",text,"\033[0m", end="", sep="")
  elif color == "yellow":
    print("\033[33m",text,"\033[0m", end="", sep="")
  elif color == "purple":
    print("\033[35m",text,"\033[0m", end="", sep="")
  elif color == "cyan":
    print("\033[36m",text,"\033[0m", end="", sep="")
  else:
    print(text, end="", sep="")

print("Super Subroutine")
print()
myPrint("With my ", "yellow")
myPrint("new program ", "purple")
myPrint("I can just call ", "yellow")
myPrint("""myPrint("and", "red") ""","yellow")
myPrint("and ", "red")
myPrint("that word will appear in the color I set it to ", "yellow")
myPrint("with no ", "green")
myPrint("weird gaps.", "cyan")
print()
print()
myPrint("Epic.\n","blue")