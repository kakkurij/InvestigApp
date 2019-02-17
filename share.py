

class share:

    def __init__(self, company, currentValue, lowestValue, highestValue, procentage):
        self.company = company
        self.price = currentValue
        self.lowest = lowestValue
        self.highest = highestValue
        self.change = procentage

    def __repr__(self):
        return self.company + ", last price: " + self.price

    def updatePrice(self, newPrice):
        self.price = newPrice
