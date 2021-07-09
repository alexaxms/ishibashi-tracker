import os

import requests
from bs4 import BeautifulSoup
import time


def get_last_state_with_datetime(shipping_code):
    r = requests.get(
        f'https://trackings.post.japanpost.jp/services/srv/search/direct?searchKind=S004&locale=en&reqCodeNo1={shipping_code}')
    soup = BeautifulSoup(r.text, 'html.parser')
    last_state = soup.findAll('td', class_="w_150")[-1].contents[0]
    last_state_datetime = soup.findAll('td', class_="w_120", rowspan="2")[-1].contents[0]
    return f'Last State: {last_state}\nDatetime: {last_state_datetime}'


def send_to_telegram(chat_id, message):
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}/sendMessage?chat_id={chat_id}&text={message}"
    requests.post(url)


if __name__ == '__main__':
    start_time = time.time()
    tracking_number = os.getenv('TRACKING_NUMBER')
    chat_id = os.getenv('CHAT_ID')
    while True:
        message = get_last_state_with_datetime(tracking_number)
        send_to_telegram(chat_id, message)
        time.sleep(3600.0 - ((time.time() - start_time) % 3600.0))
