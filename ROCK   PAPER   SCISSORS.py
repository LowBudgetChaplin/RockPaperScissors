#                                            ROCK   PAPER   SCISSORS
import random

print("ROCK  -  PAPER  -  SCISSORS \n        with Bob\n")

list = ["rock" , "paper" , "scissors"]
print("rock" , "    paper" , "    scissors\n")

user_choice = input("Choose one of the above: ")
bob_choice = random.choice(list)

print("Bob: " + bob_choice)


match user_choice:
    case "paper":
        if bob_choice == "rock":
            print("Bob: You win! :(")
        elif bob_choice == "scissors":
            print("Bob: You lose! :)")
        else:
            print("Bob: It's a draw! ;)")

    case "rock":
        if bob_choice == "paper":
            print("Bob: You lose! :)")
        elif bob_choice == "scissors":
            print("Bob: You win! :(")
        else:
            print("Bob: It's a draw! ;)")

    case "scissors":
        if bob_choice == "rock":
            print("Bob: You lose! :)")
        elif bob_choice == "paper":
            print("Bob: You win! :(")
        else:
            print("Bob: It's a draw! ;)")

