myBill = float(input("What was the bill?: "))
tip = float(input("What percentage would you like to tip?: "))
totalBill = myBill * (1 + (tip/100))
print("Total Bill (including tip): ", totalBill)
numberOfPeople = int(input("How many people?: "))
answer = totalBill / numberOfPeople
answer = round(answer,2)
print("You all owe", answer)