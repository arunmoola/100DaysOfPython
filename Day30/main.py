print ("30 Days Down")
print()

for i in range(1, 5):
  answer = input(f"How was your Day {i}: ")
  print()
  response = f"You thought Day {i} was {answer}"
  print(f"{response: ^40}")
  print()

print()
print("That's all for today")