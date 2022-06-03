from optimal_change import optimal_change
print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

print("3:", optimal_change(99, 100) == "The optimal change for an item that costs $99 with an amount paid of $100 is 1 $1 bill.")

print("4:", optimal_change(99, 50) == False)

print("5:", optimal_change(10, 10) == "The optimal change for an item that costs $10 with an amount paid of $10 is 0.")

print("6:", optimal_change(3.17, 100) == "The optimal change for an item that costs $3.17 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 1 $1 bill, 3 quarters, 1 nickel, and 3 pennies.")


