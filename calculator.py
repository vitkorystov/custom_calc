

class Calculator:
    def __init__(self):
        self.taxes = {'UT': 6.85, 'NV': 8.0, 'TX': 6.25, 'AL': 4.0, 'CA': 8.25}
        self.discounts = [[1000, 3], [5000,  5], [7000, 7], [10000, 10], [50000, 15]]

    def _get_tax(self, value):
        """определим ставку налога"""
        if value in self.taxes:
            return self.taxes[value]

    def _get_price_with_discount(self, goods_number, piece_price):
        """ получить цену со скидкой """
        try:
            discount = None
            if float(piece_price) and int(goods_number):
                price_without_discount = float(piece_price)*int(goods_number)
                if price_without_discount < self.discounts[0][0]:
                    discount = 0
                elif price_without_discount >= self.discounts[-1][0]:
                    discount = self.discounts[-1][1]
                else:
                    for i, row in enumerate(self.discounts):
                        if i < len(self.discounts)-1 and row[0] <= price_without_discount < self.discounts[i+1][0]:
                            discount = row[1]
                return None if discount is None else price_without_discount - price_without_discount*(discount/100)
        except ValueError:
            return None

    def get_prices(self, goods_number, piece_price, state_code):
        """ цены: со скидкой и с учетом налогов """
        tax = self._get_tax(state_code)
        price_with_discount = self._get_price_with_discount(goods_number, piece_price)
        if None not in (tax, price_with_discount):
            final_price = price_with_discount + price_with_discount*tax/100
            return {'price_with_discount': price_with_discount,
                    'final_price': final_price
                    }

