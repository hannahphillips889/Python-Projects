print("What is the name of player 1")
player1 = raw_input()
print("What is the name of player 2")
player2 = raw_input()
print("Player 1 is " + player1)
print("Player 2 is " + player2)

print("Player 1 please select either rock, paper, scissors")
answer = raw_input()
print("Player 2 please select either rock, paper, scissors")
answer2 = raw_input()


if answer == "rock" and answer2 == "paper":
    print("Player 2 is the winner")
elif answer == "rock" and answer2 == "scissors":
    print("Player 1 is the winner")
elif answer == "rock" and answer2 == "rock":
    print("Player 1 and Player 2 are tied")
elif answer == "paper" and answer2 == "rock":
    print("Player 1 is the winner")
elif answer == "paper" and answer2 == "scissors":
    print("Player 2 is the winner")
elif answer == "paper" and answer2 == "paper":
    print("Player 1 and Player 2 are tied")
elif answer == "scissors" and answer2 == "paper":
    print("Player 1 is the winner")
elif answer == "scissors" and answer2 == "scissors":
    print("Player 1 and Player 2 are tied")
elif answer == "scissors" and answer2 == "rock":
    print("Player 2 is the winner")
          
print("Congratulations")
