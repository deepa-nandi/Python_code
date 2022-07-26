import random as r

player1 = input("Player 1 - Select your choice: Rock, Paper, Scissors: ").lower()
player2 = r.choice(["Rock", "Paper", "Scissors"]).lower()
print("Player 2 selected: ", player2)

if (player1 == "Scissors" and player2 == "Paper"):
    print ("Player 1 is winner")

elif (player1 == "Rock" and player2 == "Scissors"):
    print ("Player 1 is winner")
    
elif (player1 == "Paper" and player2 == "Rock"):
    print ("Player 1 is winner")
    
elif (player1 == player2):
    print ("Tie.")

else:
    print ("Player 2 is winner")
