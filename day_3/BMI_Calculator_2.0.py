height = float(input("Please enter your height in m: "))
weight = float(input("Please neter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 28:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 33:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
