import requests

APP_ID = 'SAU APP_ID'
CLIENT_SECRET = 'SUA CLIENT_SECRET'

AUTH_URL = 'https://api.mercadolibre.com/oauth/token'


def get_token(code):
    data = dict(
        client_id=APP_ID,
        client_secret=CLIENT_SECRET,
        grant_type='authorization_code',
        code=code,
        redirect_uri='http://localhost:8000'
    )

    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = send_request('POST', url=AUTH_URL, data=data, headers=header)
    return response


def get_request_header(request):
    if not 'access_token' in request.session:
        token = get_token(request.session['code'])
        if not token:
            del request.session['code']
            return
        request.session['access_token'] = token.json()['access_token']

    return {'Authorization': 'Bearer ' + request.session['access_token']}


def send_request(type, url, private_url=False, request=None, headers=None, data=None):
    try:
        if not headers and private_url:
            header = get_request_header(request)
        else:
            header = headers
        return requests.request(method=type, url=url, headers=header, data=data)
    except:
        raise ConnectionError("Couldn't send the request to API.")
