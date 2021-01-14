from flask import Flask
from flask import render_template
from flask import request
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/', methods=['POST', 'GET'])
def index():
    # параметры калькулятора
    goods_number = ''
    piece_price = ''
    state_code = ''

    # результат-метки в ответе сервера на страницу
    price_with_discount_label = ''
    price_final_label = ''
    error_label = ''

    if request.method == 'GET':

        goods_number = '' if request.args.get('goodsNumber') is None else request.args.get('goodsNumber')
        piece_price = '' if request.args.get('piecePrice') is None else request.args.get('piecePrice')
        state_code = '' if request.args.get('stateCode') is None else request.args.get('stateCode')

        prices = calc.get_prices(goods_number, piece_price, state_code)

        if prices is not None:
            price_with_discount_label = f'Ваша цена со скидкой: {prices["price_with_discount"]} $'
            price_final_label = f'Итоговая цена: {prices["final_price"]} $'
        else:
            error_label = '' if [goods_number, piece_price, state_code] == ['', '', ''] else 'Проверьте вводимые данные!'

    return render_template('index.html',
                           goods_number=goods_number,
                           piece_price=piece_price,
                           state_code=state_code,
                           price_with_discount_label=price_with_discount_label,
                           price_final_label=price_final_label,
                           error_label=error_label)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
