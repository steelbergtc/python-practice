#import random module to generate random computer choice
import random;

#loop the game forever (until the player exits)
while True:
    #get user input, convert it to lower case, and validate the choice (must re-enter if not valid)
    player = raw_input("Enter your choice: rock, paper, or scissors? Or type QUIT to quit. ");
    player = player.lower();
    while (player != "rock" and player != "paper" and player != "scissors" and player != "quit"):
        print(player + " is not valid.");
        player = raw_input("Please enter another choice: rock, paper, or scissors? ");
        player = player.lower();

    #generate a random number (0, 1, or 2) and associate it with a choice
    computerInt = random.randint(0,2);
    if (computerInt == 0):
        computer = "rock";
    elif (computerInt == 1):
        computer = "paper";
    elif (computerInt == 2):
        computer = "scissors";
    else:
        computer = "Error";

    #print the answers before checking them
    if player != "quit":
        print("You chose " + player + ". \nComputer chose " + computer + ".");

    #check the answers against each other and decide on a winner
    if (player == computer):
        print("It's a draw! \nThank you for playing.")
    elif (player == "rock"):
        if (computer == "paper"):
            print("Computer wins! \nThank you for playing.");
        else:
            print("You win! \nThank you for playing.")
    elif (player == "paper"):
        if (computer == "scissors"):
            print("Computer wins! \nThank you for playing.");
        else:
            print("You win! \nThank you for playing.")
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins! \nThank you for playing.");
        else:
            print("You win! \nThank you for playing.")
    elif (player == "quit"):
        quit();
