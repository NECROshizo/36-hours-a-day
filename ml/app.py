import requests
import time

import schedule

from setting import create_logger
from setting import Setting as st
from model import matching


def get_address(resource: str) -> str:
    return f'http://{st.HOST}:{st.PORT}/api/{st.API_VERSION}/{resource}'


def get_data(url) -> dict[str, list[dict]]:
    """Функция для получения dealer_priсe и product"""
    address = get_address(url)
    _logger.warning(f'Get to {address}')
    product_data = requests.get(address)

    if product_data.status_code != 200:
        raise Exception(f' Status: {product_data.status_code}')
    return product_data.json()


def post_data(url: str, data: list[dict]) -> None:
    """Функция для отправки итогового результата"""
    address = get_address(url)
    _logger.warning(f'Post to {address}')
    requests.post(address, json={'result': data})


def main():
    data = get_data(st.URL_GET)

    dealer_prices = data['dealer_priсe']
    _logger.warning(f'Received {len(dealer_prices)} dealer_priсes')

    products = data['product']
    _logger.warning(f'Received {len(products)} products')

    _logger.warning('Start matching')
    result = matching(dealer_prices, products)
    _logger.warning('End matching')

    post_data(st.URL_POST, result)



if __name__ == '__main__':
    _logger = create_logger()
    schedule.every().day.at(st.START_TIME).do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
