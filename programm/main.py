import requests
from bs4 import BeautifulSoup
import re
import unicodedata

# Потребуется для формирования html

html_open = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
'''
html_close = '''
</body>
</html>
'''

# Главная функция


def main():
    # Собираем офферы
    # Подключение
    headers = {"API-Key": "e60a98867d363b0d43b9e7c58ec498ed", }
    url_offer = 'http://api.cpanomer1.affise.com/3.0/offers?limit=200'
    r = requests.get(url_offer, headers=headers)
    print('Формируем список офферов')

    # Ждем 200 OK
    if r.status_code == 200:
        print('status: ' + str(r.status_code))
        data = r.json()
        offers = data["offers"]     # Кладем офферы в список

        offers_list = []

        for offer in offers:
            dl = (offer["description_lang"])    # В этом ключе могут быть страны
            ru_t = dl["ru"]
            html = html_open + ru_t + html_close        # Формируем html для создания объекта soup
            soup = BeautifulSoup(html, 'lxml')
            p_in = soup.find('strong', text=re.compile('ГЕО'))  # Ищем тэг <strong> в котором содержится строка 'ГЕО'
            o_id = (offer["id"])
            o_offer_id = offer["offer_id"]
            if str(p_in) != 'None':     # Если объект не пустой, то парсим содержимое родительского тега
                geo_descr = (p_in.find_parent().get_text().strip())
            else:
                geo_descr = 'No geo is description'
            if "countries" in offer:        # Проверка наличия ключа "countries"
                geo_countries = offer["countries"]
            else:
                geo_countries = '''No key "countries" in this offer'''
            # Формируем словарь и кладем его в список
            offer_dict = {"id": o_id, "offer_id": o_offer_id, "geo_descr": unicodedata.normalize("NFKD", geo_descr.encode('utf-8').decode()), "geo_countries": geo_countries}
            offers_list.append(offer_dict)

    else:
        print('No 200 OK')

    # Собираем конверсии
    # Подключение
    url_conversion = 'http://api.cpanomer1.affise.com/3.0/stats/conversions?date_from=01-10-2017'
    r = requests.get(url_conversion, headers=headers)

    print('Формируем список конверсий')

    # Ждем 200 OK
    if r.status_code == 200:
        print('status: ' + str(r.status_code))
        data = r.json()
        conversions = data["conversions"]
        conversions_list = []       # Кладем конверсии в список

        for conv in conversions:
            # Собираем данные о конверсии
            conversion_id = conv["conversion_id"]
            conv_o_id = conv["offer"]["id"]
            country_name = conv["country_name"]
            city = conv["city"]
            ip = conv["ip"]
            # Проверка наличия ключа "clickid"
            if "clickid" in conv:
                click_id = conv["clickid"]
            else:
                click_id = '''No "clickid" key in conversion'''
            # Формируем словарь и кладем его в список
            conversion_dict = {"conversion_id": conversion_id, "offer_id": conv_o_id, "counrty_name": country_name, "city": city, "ip": ip, "clickid": click_id}
            conversions_list.append(conversion_dict)

        # Сравнение списков конверсий и офферов и вывод совпадений и данных об оффере и коверсии
        print('Поиск конверсии по офферам')
        for offer in offers_list:
            for conv in conversions_list:
                if offer["id"] == conv["offer_id"]:
                    print('-----Найдено совпадение-----')
                    print('offer_info: ')
                    print(offer)
                    print('conversion_info: ')
                    print(conv)
                    print('----------------------------')
                else:
                    continue

        print('Список офферов')
        print(offers_list)

if __name__ == "__main__":
    main()
