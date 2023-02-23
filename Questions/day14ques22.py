#  Write a class to represent an ATM machine.

class ATM:
    def __init__(self, bank, location, balance, card, pin, cash):
        self.bank = bank
        self.location = location
        self.balance = balance
        self.card = card
        self.pin = pin
        self.cash = cash