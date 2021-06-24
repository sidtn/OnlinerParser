import requests
from collections import OrderedDict
import time


t = time.time()

headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
}

def get_data(index):
    url = 'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?order=price:asc&page=1'
    r = requests.get(url=url, headers=headers)

    page = r.json()['page']
    page_count = page['last']


    dict_price = {}

    for page in range(1, page_count + 1):
        url = f'https://catalog.onliner.by/sdapi/catalog.api/search/videocard?order=price:asc&page={page}'
        r = requests.get(url=url, headers=headers)
        data = r.json()
        count_pozition = 3
        products = data['products']
        for product in products:
            if f' {index} ' in product['name'] and len(dict_price) <= count_pozition - 1:
                html_url = product['html_url']
                product_name = product['extended_name']
                prices = product['prices']
                offers = prices['offers']
                count = offers['count']
                price_min = prices['price_min']
                amount = price_min['amount']
                dict_price[float(amount)] = f'{product_name}, {html_url}'

    dict_p = (OrderedDict(sorted(dict_price.items(), key=lambda t: t[0]))).items()
    return dict_p
