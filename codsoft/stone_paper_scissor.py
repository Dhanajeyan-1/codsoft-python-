import random
computer_score=0
user_score=0
a=input("Do you want to play(yes/no):").lower()
while a=="yes":
    user=input("Choose stone, paper, or scissor: ").lower()
    B = ["stone", "paper", "scissor"]
    computer = random.choice(B)
    print(f"COMPUTER:{computer}")
    if(user==computer):
        print("match is tie")
    elif(user=="paper" and computer=="stone") or (user=="rock" and computer=="scissor") or (user=="scissor" and computer=="paper"):
        print("YOU WON")
        user_score+=1
    else:
        print("computer wins")
        computer_score+=1
    a=input("Do You Want To Continue(Yes/No):").lower()
else:
    print(f"YOUR SCORE Is :{user_score}")
    print(f"COMPUTER SCORE IS {computer_score}")
    if user_score>computer_score:
        print("Nice play")
    else:
        print("Better luck next time")
    print("Thankyou for playing")