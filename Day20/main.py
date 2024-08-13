start = int(input("Enter a starting number: "))
end = int(input("Enter the ending number: "))
increment = int(input("Enter the increment: "))

if (start > end) and increment > 0:
  print ("Invalid input")
else:
  for i in range(start, end + 1, increment):
    print(i)