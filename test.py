import unittest

from main import MortgageCalculator


class TestMortgageCalculator(unittest.TestCase):
    def test_mouthly_payment_standart(self):
        calculator = MortgageCalculator(100000, 5, 30)
        payment = calculator.mountly_payment()
        self.assertAlmostEqual(payment, 536.82, places=2)

    def test_mouthly_payment_high_interest(self):
        calculator = MortgageCalculator(100000, 10, 30)
        payment = calculator.mountly_payment()
        self.assertAlmostEqual(payment, 877.57, places=2)

    def test_mouthly_payment_short_term(self):
        calculator = MortgageCalculator(100000, 5, 15)
        payment = calculator.mountly_payment()
        self.assertAlmostEqual(payment, 790.79, places=2)

    def test_mouthly_payment_low_principal(self):
        calculator = MortgageCalculator(100000, 5, 35)
        payment = calculator.mountly_payment()
        self.assertAlmostEqual(payment, 268.41, places=2)
