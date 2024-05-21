import requests


def calling_a_request(method, address):
    """Вызов запроса URL в зависимости от выбранного метода"""
    if method == 'get':
        result = requests.get(address)
        return result.status_code
    result = requests.post(address)
    return result.status_code
