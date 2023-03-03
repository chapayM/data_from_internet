def good_name_clear(good_name):
    new_good_name = ''
    for el in good_name:
        new_good_name += el.replace('\n', '').strip()
    return new_good_name

def price_clear(price):
    new_price = ''
    new_currency = ''
    for block in price:
        if new_price == '':
            for el in block:
                if el.isdigit():
                    new_price += el
        if new_currency == '':
            for el in block:
                if 1040 <= ord(el) <= 1103:
                    new_currency += el
    return {'price': new_price, 'currency': new_currency}