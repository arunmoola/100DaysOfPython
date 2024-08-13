name = input("Name: ")
if name == "Dave" or "dave":
  print("Hi Dave")

name = input("What is your name? ")
day = input("What is the day of the week? ")

if day == "monday" or day == "MONDAY":
  favFood = input("What is your favorite food, "+name+"? ")
  print("It's {}! Day to enjoy your favorite food {}!".format(day,favFood))
elif day == "tuesday" or day == "TUESDAY":
  favSport = input("What is your favorite sport, "+name+"? ")
  print("It's {}! Time to play {}".format(day,favSport))
elif day == "wednesday" or day == "WEDNESDAY":
  favColor = input("What is your favorite color, "+name+"? ")
  print("It's {}! Time to paint with {}".format(day,favColor))  
elif day == "thursday" or day =="THURSDAY":
  favSubject = input("What is your favorite subject, "+name+"? ")
  print("It's {}! Time to learn {}!".format(day,favSubject))
elif day == "friday" or day == "FRIDAY":
  favMovie = input("What is your favorite movie, "+name+"? ")
  print("It's {}! Day for watching {}!".format(day,favMovie))
elif day == "saturday" or day == "SATURDAY":
  favSong = input("What is your favorite song, "+name+"? ")
  print("It's {}! Listen to {}, {}!".format(day,favSong,name))
elif day == "sunday" or day == "SUNDAY":
  favAnimal = input("What is your favorite animal, "+name+"? ")
  print("It's {}! Lets go to the zoo & see {}!".format(day,favAnimal))
else:
  print("That's not a day of the week!")