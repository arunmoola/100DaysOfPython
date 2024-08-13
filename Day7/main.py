print("Welcome to Fan Questions Challenge!")
print()
show = input("What is your favorite tv show? ")
if show == "The Office":
    print("That's my favorite too!")
    favChar = input("Who is your favorite character? ")
    if favChar == "Michael":
      print("Michael Rocks!")
    elif favChar == "Jim":
      print("Michael does better than Jim!")
    else:
      print("That's a cool character!")
elif show == "Friends":
  print("I love Friends too!")
  favChar = input("Who is your favorite character? ")
  if favChar == "Chandler":
    print("Chandler Rocks!")
  elif favChar == "Joey":
    print("Chandler does better than Joey!")
  else:
    print("That's a cool character!")
else:
  print("That's a great show!")
print()
print("Thanks for playing!")