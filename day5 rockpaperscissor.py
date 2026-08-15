import random
items=["rock","paper","scissor"]
computer=random.choice(items)
user=input("Rock Paper or Scissor: ").lower()
print("computer choose",computer)
if user==computer:
    print("Match Draw.......!")
elif user=="rock" and computer =="scissor":
    print("user winnnn !")
elif user=="paper" and computer =="rock":
    print("user winnnn !")
elif user=="scissor" and computer =="paper":
    print("user winnnn !")
else:
    print("computer win")
