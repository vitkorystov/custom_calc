import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_bad_state(self):
        self.assertIsNone(self.calculator.get_prices('500', '10', 'ggg'))

    def test_bad_empty(self):
        self.assertIsNone(self.calculator.get_prices('', '', ''))

    def test_bad_not_number_for_goods_number(self):
        self.assertIsNone(self.calculator.get_prices('rrt', '500', 'TX'))

    def test_bad_not_number_for_piece_price(self):
        self.assertIsNone(self.calculator.get_prices('50', 'ccc', 'TX'))

    def test_price_less_then_1000(self):
        self.assertEqual(self.calculator.get_prices('5', '100', 'TX')['price_with_discount'], 500)

    def test_price_more_then_60000(self):
        self.assertEqual(self.calculator.get_prices('6', '10000', 'TX')['price_with_discount'], 51000)

    def test_common_price_price_with_discount(self):
        self.assertEqual(self.calculator.get_prices('4', '1000', 'TX')['price_with_discount'], 3880)

    def test_common_price_final_price(self):
        self.assertEqual(self.calculator.get_prices('4', '1000', 'TX')['final_price'], 4122.5)


if __name__ == '__main__':
    unittest.main()
