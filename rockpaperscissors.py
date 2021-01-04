import random


def rock_paper_scissors():

    while True:

        choice = input("Rock (r), paper (p), scissors (s)? ")
        comp_choice = random.choice(['r', 'p', 's'])
        full_name = ''

        if comp_choice == 'r':
            full_name = "rock"
        elif comp_choice == 's':
            full_name = "scissors"
        else:
            full_name = "paper"

        print(f"Computer's choice is: {full_name}")

        if choice == comp_choice:
            print("It's a tie!")

        elif winning(choice, comp_choice):
            print("You win!")

        else:
            print("You lost!")

        game_on = input("Again? (y/n)? ")
        if game_on == 'n':
            return


def winning(player, computer):
    if (player == 'r' and computer == 's' or
            player == 's' and computer == 'p' or
            player == 'p' and computer == 'r'):
        return True

    else:
        return False


rock_paper_scissors()

