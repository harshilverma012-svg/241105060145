print("Commission Engine")
sales = int(input("Enter total sales: "))
target = int(input("Enter target: "))
if sales >= target * 2:
    commission = sales * 20 / 100
elif sales >= target:
    commission = sales * 10 / 100
elif sales >= target / 2:
    commission = sales * 5 / 100
else:
    commission = 0
bonus = commission * 10 / 100
final = commission + bonus
print("Commission:", commission)
print("Bonus:", bonus)
print("Final Commission:", final)
if final > sales:
    print("Calculation error")
if sales == 0:
    print("No sales made")
