import classes_module as cm
import functions_module as func

chips = 100

while True:
    if chips == 0:
        print(f"You lost all your chips")
        break
    hit_stand = 0
    deck = cm.CardDeck()
    deck.shuffle_all_cards()
    player = cm.Player("Player")
    dealer = cm.Player("Dealer")

    chips_bet = func.chips_bet_value_check(chips)

    print(f"You bet {chips_bet} out of your {chips} total\n")

    for x in range(2):
        player.draw_card(deck)
        dealer.draw_card(deck)
    # Kjører funksjonen for å total verdi hver gang ett kort blir trukket, siden denne metoden inneholder
    # sjekken for om Ace skal være 1 eller 11
    player.total_hand_value()
    dealer.total_hand_value()
    print(f"The cards have been dealt. You have a {player.hand[0].show_card()} and a "
          f"{player.hand[1].show_card()} with a total value of {player.total_hand_value()}\n"
          f"The dealers visible card is a {dealer.hand[0].show_card()}\n\n")

    again, blackjack_chips, passed = func.blackjack_check(player.total_hand_value(), chips, chips_bet)

    if passed:
        chips = blackjack_chips
        if again == "y":
            continue
        else:
            break

    else:
        print(f"You did not get Black jack\n")

    hit_stand = func.hit_stand_value_check()

    if hit_stand == 1:
        while hit_stand == 1:
            player.draw_card(deck)
            player.total_hand_value()
            print(f"You have been dealt one card ({player.hand[len(player.hand) - 1].value}). "
                  f"Your hand now consists of the following cards:\n")
            player.show_hand()
            print(f"\nThe total value of your hand is {player.total_hand_value()},"
                  f" and the dealers is {dealer.hand[0].value}\n")

            result_chips, again, passed = func.result_check(player.total_hand_value(), dealer.total_hand_value(), chips,
                                                            chips_bet, 0)
            # Må ha en egen break sjekk her for at den skal gå ut av hit_stand while loopen for å så sjekke
            # spillet skal fortsette eller ikke
            if passed:
                chips = result_chips
                break
            hit_stand = func.hit_stand_value_check()
        if passed:
            if again == "y":
                continue
            else:
                break

    if hit_stand == 2:
        while dealer.total_hand_value() < 17:
            dealer.draw_card(deck)
            dealer.total_hand_value()

        print(f"The dealer draws until their hand value is greater than 17. "
              f"The dealers cards are the following:\n")
        dealer.show_hand()
        print(f"\nThe total value of the dealers hand is {dealer.total_hand_value()},"
              f" compared to your {player.total_hand_value()}")

    result_chips, again, passed = func.result_check(player.total_hand_value(), dealer.total_hand_value(), chips,
                                                    chips_bet, 1)

    if passed:
        chips = result_chips
        if again == "y":
            continue
        else:
            break

    print('continure')
