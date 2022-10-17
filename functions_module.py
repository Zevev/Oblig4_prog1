def blackjack_check(value, total_chips, chips_bet):
    if value == 21:
        total_chips += int(chips_bet) * 2
        print(f"Blackjack! You got {value}, your total chips is now {total_chips}")
        again = play_again_check()
        return again, total_chips, True

    else:
        return "s", 11, False


def result_check(player_value, dealer_value, chips, bet, hit_or_stand):
    win = False
    lose = False
    if player_value > 21:
        lose = True

    elif dealer_value > 21:
        win = True

    elif 21 >= dealer_value > player_value and hit_or_stand == 1:
        lose = True

    elif 21 >= player_value > dealer_value and hit_or_stand == 1:
        win = True

    elif player_value == dealer_value and hit_or_stand == 1:
        print(f"No one wins. You keep your chips")
        again = play_again_check()
        return chips, again, True

    if win:
        print(f"You won! You gain {bet} chips, your total is now {int(chips) + int(bet)}")
        again = play_again_check()
        return int(chips) + int(bet), again, True
    elif lose:
        print(f"You lost! You lose {bet} chips, your total is now {int(chips) - int(bet)}")
        again = play_again_check()
        return int(chips) - int(bet), again, True

    else:
        return chips, "0", False


def hit_stand_value_check():
    while True:
        hit_stand = input(f"Do you wish to hit or stand?\n"
                          f"1 - Hit\n"
                          f"2 - Stand\n"
                          f"Answer:")
        try:
            hit_stand = int(hit_stand)
        except ValueError:
            print("please enter a number\n")
            continue
        if hit_stand == 1 or hit_stand == 2:
            break
        else:
            print("Please enter 1 for Hit or 2 for Stand\n")
    return hit_stand


def chips_bet_value_check(chips):
    while True:
        chips_bet = input(f"You currently have {chips} chips. How many do you want to bet?\n")
        try:
            chips_bet = int(chips_bet)
        except ValueError:
            print("Please enter a number")
            continue
        if 0 < chips_bet <= chips:
            break
        else:
            print(f"Please enter a number between 1 and {chips}")
    return chips_bet


def play_again_check():
    while True:
        again = input(f"Do you wish to play again?\n"
                      f"y - Yes\n"
                      f"n - No\n")
        if again == "y" or again == "n":
            break
        else:
            print(f"Please enter 'y' or 'n'")
    return again
