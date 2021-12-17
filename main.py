
print("Welcome to the tip calculator!")
totalBill = float((input("What was the total bill?")))
split = float((input("How many people to split the bill?")))
tip = float((input("What percentage tip would you like to give? 10, 12 or 15?")))
totalTip = tip/100 * totalBill 
tipAdded = totalBill + totalTip

totalForEach = "{:.2f}".format(round(tipAdded / split, 2))
print(totalForEach)
