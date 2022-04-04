class Atm:
    def __init__(self, cardNumber, pin, expirationDate):
        self.cardNumber = cardNumber
        self.pin = pin
        self.expirationDate = expirationDate

    def card_number(self):
        return("Your card number is ", self.cardNumber)

    def Pin(self):
        return("Your pin is ", self.pin)

    def expiration_date(self):
        return("Your card expires on ", self.expirationDate)

a = Atm(12345678910, 9876, "January 1st, 2025")

print(a.cardNumber)
print(a.Pin())
print(a.expiration_date())
