import random

choice = { 1: "rock",
          2: "paper", 
          3: "scissors" }


comp = random.choice(list(choice.keys()))

you = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))

if you not in choice:
    print("Invalid choice. Please enter 1, 2, or 3.")
else: 
    if you == comp and you in choice:
        print(f"Both chose {choice[you]}. It's a tie!")
    elif (you == 1 and comp == 3) or (you == 2 and comp == 1) or (you == 3 and comp ==2):
        print(f"You win! {choice[you]} beats {choice[comp]}.")
    else:
        print(f"You lose! {choice[comp]} beats {choice[you]}.")
        print(f"You chose {choice[you]}, computer chose {choice[comp]}.")
print("Thanks for playing!")