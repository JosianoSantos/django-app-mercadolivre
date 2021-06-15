from api.mercado_libre.auth import send_request


def get_most_expensives_by_category(category, test=False):
    response = send_request('GET',
                            url='https://api.mercadolibre.com/sites/MLA/search?category={}&sort=price_desc&limit=50'.format(
                                category))

    if test:
        return response

    if response:
        return response.json()
    else:
        raise ConnectionError('Error on getting most expensives items.Try again.')


def get_best_sellers_by_item_category(category, test=False):
    response = send_request('GET',
                            url='https://api.mercadolibre.com/sites/MLA/search?category={}&limit=50'.format(category))

    if test:
        return response

    if response:
        return response.json()['results']
    else:
        raise ConnectionError('Error on getting best selles.Try again.')
