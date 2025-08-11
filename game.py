import random

choice = { 1: "rock",
          2: "paper", 
          3: "scissors" }

highscore = open("highscore.txt", "a+")
highscore.seek(0)
current_high = highscore.read()

if current_high == "":
    highscore.seek(0)
    current_high = "0"
else:
    current_high= int(current_high)




play = "yes"
score = 0

while play == "yes":
    play = input("Do you want to play rock, paper, scissors? (yes/no): ").lower()
    if play not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
        continue
    elif play == "yes":
        comp = random.choice(list(choice.keys()))
        you = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
        
        if you not in choice:
            print("Invalid choice. Please enter 1, 2, or 3.")
        else: 
            if you == comp and you in choice:
                print(f"Both chose {choice[you]}. It's a tie!")
            elif (you == 1 and comp == 3) or (you == 2 and comp == 1) or (you == 3 and comp ==2):
                print(f"You win! {choice[you]} beats {choice[comp]}.")
                score += 1
                print(f"You chose {choice[you]}, computer chose {choice[comp]}.")
            else:
                print(f"You lose! {choice[comp]} beats {choice[you]}.")
                print(f"You chose {choice[you]}, computer chose {choice[comp]}.")
                if score > 0:
                    score -= 1
    else:
        break

if(int(current_high) < score):
    highscore.seek(0)
    highscore.write(str(score))
    highscore.truncate()
    print(f"New high score: {score}")
print("Thanks for playing!")
highscore.close()