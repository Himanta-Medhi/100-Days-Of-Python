print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split = float(input("How many people to split the bill? "))

each_person_amount = total_bill*(1 + tip/100) / split

rounded_amount = f"{each_person_amount:.2f}" #This rounds the amount till 2 digits after decimal.


print(f"Each person should pay: ${rounded_amount}")

