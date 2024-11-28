class MortgageCalculator:
    def __init__(self, principial, annual_rate, years):
        self.principal = principial
        self.mouthly_rate = annual_rate / 12 / 100
        self.mounts = years * 12

    def mountly_payment(self):
        if self.mouthly_rate == 0:
            print()
            return self.principal / self.mounts
        return (self.principal * self.mouthly_rate) / (1 - (1 + self.mouthly_rate) ** -self.mounts)