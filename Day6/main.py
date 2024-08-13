user = input("Username>")
pwd = input("Password>")

if user == "admin" and pwd == "password":
    print("Welcome Admin!")
elif user == "arun" and pwd == "h@ck3r":
  print("Welcome Arun!")
elif user == "john" and pwd == "d0e123":
  print("Welcome John Doe!")
else:
    print("Access denied")