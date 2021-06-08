import random

if __name__ == '__main__':
    class Deck(object):
        def __init__(self):
            self.cards = []
            self.generate_cards()

        def __iter__(self):
            return iter(self.cards)

        def __getitem__(self, index):
            return self.cards[index]

        # The Deck class should display only the number of cards there are still in the deck when printed
        def __str__(self):
            return f'{len(self.cards)}'

        # There should be a shuffle method which makes sure the deck of cards has all 52 cards (throws error otherwise)
        # and then rearranges them randomly.
        def shuffle_cards(self):
            if len(self.cards) == 52:
                return random.shuffle(self.cards)
            else:
                raise Exception(f"There are {len(self.cards)} cards in the deck instead of 52")

        # The Deck class should have a deal method to deal a single card from the deck
        # After a card is dealt, it is removed from the deck.
        def deal_card(self):
            removed_card = self.cards.pop()
            return removed_card

        def generate_cards(self):
            for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                for value in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                    self.cards.append(Card(value, suit))


    class Card(object):
        # The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit

        # The Card class should display it's type when printed : e.g. 2 of Diamonds
        def __str__(self):
            return f'{self.value} of {self.suit}'


    deck_of_cards = Deck()
    print(deck_of_cards)
    deck_of_cards.shuffle_cards()
    dealt_card = deck_of_cards.deal_card()
    print(dealt_card)
    # raise exception
    deck_of_cards.shuffle_cards()
