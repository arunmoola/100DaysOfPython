principal = 1000
rate = float(5 / 100)

for year in range(10):
  principal = principal * (1 + rate)
  print("At the end of year {}: {}".format(year+1,round(principal,2)))