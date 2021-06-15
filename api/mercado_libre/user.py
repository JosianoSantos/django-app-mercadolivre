from api.mercado_libre.auth import send_request


def get_logged_user_data(request):
    response = send_request('GET', private_url=True, url='https://api.mercadolibre.com/users/me', request=request)
    if response:
        return response.json()
    else:
        raise ConnectionError('Error on getting user data.Try again.')


def get_user_detail_by_id(id):
    response = send_request('GET', url='https://api.mercadolibre.com/users/{}'.format(id))
    if response:
        return response.json()
    else:
        raise ConnectionError('Error on getting user details.Try again.')
