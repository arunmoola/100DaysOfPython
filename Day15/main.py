exit = ""
while exit != "y" and exit != "Y" and exit != "yes" and exit != "YES":
  animal = input("What animal do you want?: ")
  if animal == "cow":
    print("moo")
  elif animal == "sheep":
    print("baaa")
  elif animal == "dog":
    print("woof")
  elif animal == "cat":
    print("meow")
  elif animal == "bird":
    print("chirp")
  elif animal == "horse":
    print("neigh")
  elif animal == "pig":
    print("oink")
  else:
    print("I don't know that animal.")
  exit = input("Do you want to exit? (y/n): ")