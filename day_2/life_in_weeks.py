age = input("What is your current age ")
years = int(age) - 90
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)
message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)