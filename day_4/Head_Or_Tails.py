import random

print("Welcome to my head or tails game")
outcome = random.randint(0, 1)
if outcome == 0:
    print("It is Heads")
else:
    print("It is tails")