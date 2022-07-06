import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
items = len(names)
random_choice = random.randint(0, items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")