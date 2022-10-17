import random

symbols = ["Clubs", "Hearts", "Diamond", "Spade"]


class Card:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol

    def show_card(self):
        return f"{self.value} of {self.symbol}"

    def set_value(self, new_value):
        self.value = new_value


class CardDeck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for x in symbols:
            for y in range(1, 14):
                if y == 1:
                    self.cards.append(Card(y, "Ace"))
                elif y >= 11:
                    self.cards.append(Card(10, x))
                else:
                    self.cards.append(Card(y, x))

    def show_all_cards(self):
        for c in self.cards:
            c.show_card()

    def shuffle_all_cards(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        return self.hand

    def show_hand(self):
        for z in self.hand:
            print(f" - {z.show_card()}")

    def total_hand_value(self):
        value = 0
        for y in self.hand:
            if y.value == 1 and value + 11 <= 21:
                y.set_value(11)

            value += y.value
        return value
