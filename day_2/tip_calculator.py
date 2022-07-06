print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? €"))
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill with? "))

tip_in_percent = tip / 100
total_tip = bill * tip_in_percent
total_bill = bill + total_tip
total_per_person = total_bill / people
final_amount = "{:.2f}".format(total_per_person)
print(f"Each person should pay: €{final_amount}")