Задание:
Используя API Affise - https://api.affise.com/
и ключ авторизации e60a98867d363b0d43b9e7c58ec498ed
Получить информацию о доступном оффере. Какие страны доступны в этом оффере. Вывести список этих стран.
Также получить уже имеющуюся конверсию. Уточнить, имеющаяся в статистике, относится ли она к офферу.
Если да, то вывести ClickID конверсии, а также вывести откуда она была.
В данном API вы имеете ключ партнера, не админ.

Код выложить на гитхаб, прислать ссылку
Домен для работы : http://api.cpanomer1.affise.com

Код:



Пояснительная записка:
При анализе ответов API и анализе примеров ответов API в инструкции было обнаружено следующее:
В примере в инструкции (http://YOUR_API_DOMAIN/3.0/offers) ключ "status" присутствует, но отсутствует в ответе API при использовании токена e60a98867d363b0d43b9e7c58ec498ed
(Смотрите ниже, пункт выделен как "Примеры")

В примере в  инструкции (http://YOUR_API_DOMAIN/3.0/stats/conversions) ключ "clickid" 
присутствует, но отсутствует в ответе API при использовании токена e60a98867d363b0d43b9e7c58ec498ed
(Смотрите ниже, пункт выделен как "Примеры")

Пояснение к "status" из инструкции:
status
Array[string]
Default: active
Available: active, stopped, suspended
ONLY FOR ADMIN

Возникло непонимание в поиске доступного оффера при отсутствии признака доступности
(допускаю, что мог не увидеть этот признак, но многократное перечитывание инструкции не продвинуло меня решении вопроса).
В связи с этим, я собрал офферы и конверсии в два списка и сравнил их.
Вывел информацию о совпавших идентификаторов в офферах и в конверсии.
При выводе ответа идёт проверка на наличие ключа "clickid" в конверсии

Какие страны доступны в этом оффере. Вывести список этих стран:
Страны могут быть указаны в описании (ключ "description_lang" ) и в ключе "countries".
Список всех офферов с информаций о доступных странах из "description_lang" и из "countries"
будет выведен после вывода сравнения списков офферов и конверсий


Примеры:
---------------------------------------------------------------------------
Пример отсутствия ключа "status" в ответе от API
Пример ответа из инструкции:

curl --header "API-Key:23df424b0a53b0899f78685966243ee61" /
http://YOUR_API_DOMAIN/3.0/partner/offers

{
   "status":1,
   "offers":[
      {
         "id":902,
         "offer_id":"5718dac83b7d9bf8588b4579",
         "title":"...",
         "preview_url":"....",
         "description":"...",
         "cr":199850,
         "epc":298988.33,
         "logo":"http:\/\/affise.admin\/images\/cpa\/logos\/2602108452.png",
         "stop_at":"",
         "sources":[
            {
               "id":"51f531f53b7d9b1e0382f6d9",
               "title":"Web sites",
               "allowed":1
            }
         ],
         "categories":[
            "..."
         ],
         "full_categories":[
            {
               "id":"5368afb23b7d9b4d5d505342",
               "title":"..."
            }
         ],
         "payments":[
            {
               "countries":[
                  "US"
               ],
               "cities":[

               ],
               "country_exclude":false,
               "title":"...",
               "goal":"1",
               "revenue":150,
               "currency":"USD",
               "type":"fixed",
               "devices":[

               ],
               "os":[

               ]
            }
         ],
         "required_approval":true,
         "landings":[

         ],
         "is_cpi":false,
         "creatives":[

         ],
         "creatives_zip":null,
         "links":[
            {
               "id":null,
               "title":null,
               "hash":null,
               "url":"http:\/\/affise.tds\/click?pid=610\u0026offer_id=902",
               "postbacks":[

               ],
               "created":null
            }
         ],
         "macro_url":null,
         "link":"http:\/\/affise.tds\/click?pid=610\u0026offer_id=902",
         "use_https":false,
         "use_http":true,
         "hold_period":0,
         "caps": [
             {
                "period": "day",
                "type": "conversions",
                "value": 100,
                "goal_type": "exact",
                "goals": {
                    "1" : "Install",
                    "2" : "Register"
                 }
             },
             {
                 "period": "month",
                 "type": "budget",
                 "value": 100,
                 "goal_type": "each",
                 "goals": {}
             },
             {
                 "period": "all",
                 "type": "budget",
                 "value": 100,
                 "goal_type": "all",
                 "goals": {}
             }
         ]
      }
   ],
   "pagination":{
      "per_page":1,
      "total_count":127,
      "page":1,
      "next_page":2
   }
}

Ответ от API:

curl --header "API-Key:e60a98867d363b0d43b9e7c58ec498ed" /
http://api.cpanomer1.affise.com/3.0/offer/660


{
    "status": 1,
    "offer": {
        "id": 660,
        "offer_id": "5f16e18781198083008b4574",
        "title": "1win [Baseline 5$]",
        "preview_url": "https://1watm.top/?sub1={clickid}&sub2={pid}#gnqt",
        "description_lang": {
            "ru": "<p><strong>1win БК -&nbsp;</strong>Уже сегодня тысячи людей зарабатывают не выходя из дома.<br />\r\nВысокие коэффициенты, мгновенные выплаты, русскоязычная техническая поддержка работающая 24 часа в сутки, бонусная программа, кейсы с денежными призами и многое другое.</p>\r\n\r\n<h2><strong>Условия по офферу:</strong></h2>\r\n\r\n<h3><strong>ОБЯЗАТЕЛЬНО РЕГИСТРАЦИЯ ПО ПРОМОКОДУ, ЕСЛИ ПРОМОКОД УКАЗАН СТОРОННИЙ КОНВЕРСИЯ НЕ ЗАСЧИТЫВАЕТСЯ</strong></h3>\r\n\r\n<h3><strong>2020bets&nbsp;- для РФ</strong></h3>\r\n\r\n<h3><strong>2020cis - для СНГ</strong></h3>\r\n\r\n<p><strong>CPA FTD:&nbsp;</strong></p>\r\n\r\n<p><strong>32$ (Гео:&nbsp;РФ)</strong></p>\r\n\r\n<p><strong>28$ (Гео: СНГ+Украина)</strong></p>\r\n\r\n<p><strong>Baseline: 5$ (накопительный)</strong></p>\r\n\r\n<p><br />\r\n<strong>Время на прохождение игроком KPI: 30 дней с момента регистрации</strong></p>\r\n\r\n<p><br />\r\n<strong>Hold: 14 дней (для проверенных вебов может быть уменьшен до 7 дней)&nbsp;</strong></p>\r\n\r\n<p><strong>Тестовый лимит: 10-50 конверсий (определяется на этапе согласования источника трафика веба).&nbsp;</strong></p>\r\n\r\n<p>Cookie lifetime: 365 days<br />\r\nFirst cookie wins</p>\r\n\r\n<p><em>Запрещенные источники трафика:<br />\r\n- Мотивированный трафик, трафик с буксов<br />\r\n- Брокерский трафик<br />\r\n- Мислид<br />\r\n- Контекст на бренд<br />\r\n- ClickUnder/PopUnder<br />\r\n- Push Notifications<br />\r\n- Спам&nbsp;<br />\r\n- Тизерная реклама&nbsp;&nbsp; &nbsp;</em></p>\r\n\r\n<p><br />\r\n<em>Запрещено указывать минимальную сумму депозита в креативах</em></p>\r\n\r\n<p><em>В случае выявления нарушений рекламодатель оставляет за собой право не оплачивать трафик, либо оплатить его по индивидуальной ставке.</em></p>\r\n\r\n<p><em>При небольшом количестве конверсий у рекламодателя могут возникнуть трудности с анализом качества трафика. При неоднозначных результатах проверки трафика срок холда может быть увеличен.</em></p>\r\n\r\n<p><em>Трафик проверяется на активность, повторные депозиты. Мультиаккаунты, фрод, неактивный трафик не оплачиваются.</em></p>\r\n\r\n<p><em>При стабильном качественном трафике возможно повышение ставки в индивидуальном порядке.</em></p>",
            "en": ""
        },
        "cr": 50,
        "epc": 0,
        "logo": "http://offers.cpanomer1.affise.com/images/cpa/logos/1961720404.png",
        "logo_source": "1961720404.png",
        "stop_at": null,
        "sources": [
            {
                "id": "51f531f53b7d9b1e0382f6d9",
                "title": "Веб-сайты",
                "allowed": 1
            },
            {
                "id": "51f532053b7d9b340eea741a",
                "title": "Дорвеи",
                "allowed": 1
            },
            {
                "id": "51f532103b7d9b340e325f1c",
                "title": "Контекстная реклама",
                "allowed": 1
            },
            {
                "id": "51f5322d3b7d9b340eabb872",
                "title": "Контекстная реклама на бренд",
                "allowed": 0
            },
            {
                "id": "51f532393b7d9b5e030908a0",
                "title": "Тизерная/баннерная реклама",
                "allowed": 0
            },
            {
                "id": "51f5325e3b7d9b340e8a2b79",
                "title": "Соц.сети: таргетированная реклама",
                "allowed": 1
            },
            {
                "id": "51f532713b7d9b5e03b24520",
                "title": "Соц.сети: паблики, игры, приложения",
                "allowed": 1
            },
            {
                "id": "51f532873b7d9b5e03e88a74",
                "title": "Email-рассылка",
                "allowed": 1
            },
            {
                "id": "5432ffe43b7d9b615f4f7f2a",
                "title": "Мобильный трафик",
                "allowed": 1
            },
            {
                "id": "5432fff93b7d9b615fab559d",
                "title": "ClickUnder/PopUnder",
                "allowed": 0
            },
            {
                "id": "5433000d3b7d9b615f6392b8",
                "title": "Реброкеринг",
                "allowed": 0
            },
            {
                "id": "5433001e3b7d9b456bc15573",
                "title": "Мотивированный трафик",
                "allowed": 0
            },
            {
                "id": "5c4b1f7762aa05003c0e8f62",
                "title": "Push-трафик",
                "allowed": 0
            }
        ],
        "categories": [
            "Betting"
        ],
        "full_categories": [
            {
                "id": "5af2d6f581198049008b4627",
                "title": "Betting"
            }
        ],
        "payments": [
            {
                "countries": [
                    "RU"
                ],
                "cities": [],
                "country_exclude": false,
                "title": "fd",
                "goal": "fd",
                "revenue": 32,
                "currency": "USD",
                "type": "fixed",
                "devices": [],
                "os": []
            },
            {
                "countries": [
                    "UA",
                    "GE",
                    "KZ",
                    "TM",
                    "KG",
                    "MD",
                    "BY",
                    "AM",
                    "TJ",
                    "UZ",
                    "AZ"
                ],
                "cities": [],
                "country_exclude": false,
                "title": "fd",
                "goal": "fd",
                "revenue": 28,
                "currency": "USD",
                "type": "fixed",
                "devices": [],
                "os": []
            },
            {
                "countries": [
                    "UA",
                    "GE",
                    "KZ",
                    "TM",
                    "KG",
                    "MD",
                    "BY",
                    "RU",
                    "AM",
                    "TJ",
                    "UZ",
                    "AZ"
                ],
                "cities": [],
                "country_exclude": false,
                "title": "reg",
                "goal": "reg",
                "revenue": 0,
                "currency": "USD",
                "type": "fixed",
                "devices": [],
                "os": []
            }
        ],
        "goals": {
            "fd": "fd",
            "reg": "reg"
        },
        "caps": [],
        "caps_timezone": "Europe/Moscow",
        "hide_caps": 0,
        "required_approval": true,
        "strictly_country": 1,
        "strictly_os": null,
        "strictly_brands": null,
        "is_cpi": false,
        "kpi": {
            "ru": ""
        },
        "creatives": [],
        "creatives_zip": null,
        "landings": [
            {
                "id": 1595335047,
                "title": "Default",
                "url": "https://x.go-track.ru/click?pid=10932&offer_id=660&l=1595335047",
                "url_preview": "https://1watm.top/?sub1={clickid}&sub2={pid}#gnqt",
                "type": "landing"
            },
            {
                "id": 1595335048,
                "title": "CIS",
                "url": "https://x.go-track.ru/click?pid=10932&offer_id=660&l=1595335048",
                "url_preview": "https://1wkk.top/?sub1={clickid}&sub2={pid}#0ggy",
                "type": "landing"
            }
        ],
        "links": [
            {
                "id": null,
                "title": null,
                "hash": null,
                "url": "https://x.go-track.ru/click?pid=10932&offer_id=660",
                "postbacks": [],
                "created": null
            }
        ],
        "macro_url": "",
        "link": "https://x.go-track.ru/click?pid=10932&offer_id=660",
        "use_https": true,
        "use_http": true,
        "hold_period": 30,
        "click_session": "1y",
        "minimal_click_session": "0s",
        "disabled_choice_postback_status": false,
        "strictly_isp": [],
        "restriction_isp": null,
        "search_empty_sub": null,
        "targeting": [
            {
                "country": {
                    "allow": [
                        "RU"
                    ],
                    "deny": []
                },
                "region": {
                    "allow": [],
                    "deny": []
                },
                "city": {
                    "allow": [],
                    "deny": []
                },
                "os": {
                    "allow": [],
                    "deny": []
                },
                "isp": {
                    "allow": [],
                    "deny": []
                },
                "ip": {
                    "allow": [],
                    "deny": []
                },
                "browser": {
                    "allow": [],
                    "deny": []
                },
                "brand": {
                    "allow": [],
                    "deny": []
                },
                "device_type": [],
                "connection": [],
                "block_proxy": false
            },
            {
                "country": {
                    "allow": [
                        "UA",
                        "GE",
                        "KZ",
                        "TM",
                        "KG",
                        "MD",
                        "BY",
                        "AM",
                        "TJ",
                        "UZ",
                        "AZ"
                    ],
                    "deny": []
                },
                "region": {
                    "allow": [],
                    "deny": []
                },
                "city": {
                    "allow": [],
                    "deny": []
                },
                "os": {
                    "allow": [],
                    "deny": []
                },
                "isp": {
                    "allow": [],
                    "deny": []
                },
                "ip": {
                    "allow": [],
                    "deny": []
                },
                "browser": {
                    "allow": [],
                    "deny": []
                },
                "brand": {
                    "allow": [],
                    "deny": []
                },
                "device_type": [],
                "connection": [],
                "block_proxy": false
            }
        ],
        "schedule": {
            "enabled": false,
            "date_start": "",
            "date_to": "",
            "timezone": "Europe/Moscow"
        },
        "io_document": null,
        "consider_personal_targeting_only": false,
        "impressions_link": null,
        "uniq_ip_only": true,
        "reject_not_unique_ip": false,
        "postbacks": [],
        "pixels": [],
        "allow_deeplink": false,
        "ticket_created": true,
        "countries": [
            "RU",
            "UA",
            "GE",
            "KZ",
            "TM",
            "KG",
            "MD",
            "BY",
            "AM",
            "TJ",
            "UZ",
            "AZ"
        ]
    }
}

Можно увидеть, что ключ "status" есть в инструкции, но нет в ответе.
------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

Пример отсутствия ключа "clickid" в ответе.
curl --header "API-Key:23df424b0a53b0899f78685966243ee61" /
http://YOUR_API_DOMAIN/3.0/stats/conversions?action_id=&clickid=&country[0]=US&currency=125&custom_field_1=&custom_field_2=&custom_field_3=&custom_field_4=&custom_field_5=&custom_field_6=&custom_field_7=&date_from=01-05-2017&date_to=01-07-2017&limit=1&page=1&payouts=&revenue=&timezone=Asia/Tokyo"

{  
   "status":1,
   "conversions":[  
      {  
         "id":"59359e1d7e28feb7568b456a",
         "action_id":"59359dcb7e28fee0558b4567",
         "status":"confirmed",
         "currency":"USD",
         "goal":null,
         "country":"US",
         "district":"",
         "city":"New York",
         "ip":"127.0.0.1",
         "browser":"Chrome 58.0.3029",
         "os":"Mac OS X 10.12.5",
         "device":"Other",
         "offer":{ // Will return null if the offer doesn't exist
            "id":934,
            "offer_id":"59313e097960ad2774b4f274",
            "title":"HD-smart [Web]",
            "preview_url":"http:\/\/affise.com\/1\/"
         }, 
         "offer_id":"934",
         "ios_idfa":"",
         "android_id":"",
         "sub1":"",
         "sub2":"",
         "sub3":"",
         "sub4":"",
         "sub5":"",
         "custom_field_1":"",
         "custom_field_2":"",
         "custom_field_3":"",
         "custom_field_4":"",
         "custom_field_5":"",
         "custom_field_6":"",
         "custom_field_7":"",
         "ua":"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/58.0.3029.110 Safari\/537.36",
         "comment":"",
         "created_at":"2017-06-06 03:08:29",
         "click_time":"2017-06-06 03:07:07",
         "referrer":"http://affise.com",
         "payouts":1234,
         "clickid":"59359dcb7e28fee0558b4567",
         "partner":{  
            "id":610,
            "email":"example@gmail.com",
            "login":"example",
            "name":""
         },
         "goal_value":"1",
         "sum":0,
         "revenue":12345,
         "earnings":11111,
         "advertiser":{  
            "id":"56cc49dc3b7d9b89058b45f0",
            "title":"Example"
         },
         "payment_status":"opened",
         "is_paid":"1",
         "forensiq":null,
         "payment_type":null,
         "hold_date_expire":null
      }
   ],
   "pagination":{  
      "per_page":1,
      "total_count":17,
      "page":1,
      "next_page":2
   }
}


curl --header "API-Key:e60a98867d363b0d43b9e7c58ec498ed" /
http://api.cpanomer1.affise.com/3.0/stats/conversions?date_from=01-10-2010

{
    "status": 1,
    "conversions": [
        {
            "id": "5f2011ff811980a4008b459c",
            "action_id": "5f20117beb2d6c0001332e73",
            "status": "pending",
            "conversion_id": "5f2011ff811980a4008b459c",
            "cbid": "5f20117beb2d6c0001332e73",
            "currency": "USD",
            "offer": {
                "id": 660,
                "title": "1win [Baseline 5$]",
                "offer_id": "5f16e18781198083008b4574",
                "external_id": false
            },
            "offer_id": 660,
            "goal": "fd",
            "hold_date_expire": null,
            "ip": "178.66.66.162",
            "country": "RU",
            "country_name": "Russian Federation",
            "district": null,
            "city": "St Petersburg",
            "city_id": 18964,
            "isp_code": "-",
            "ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "browser": "Chrome 84",
            "os": "Linux ",
            "device": "desktop",
            "device_type": "desktop",
            "sub1": "",
            "sub2": "",
            "sub3": "",
            "sub4": "",
            "sub5": "",
            "sub6": "",
            "sub7": "",
            "sub8": "",
            "custom_field_1": "",
            "custom_field_2": "",
            "custom_field_3": "",
            "custom_field_4": "",
            "custom_field_5": "",
            "custom_field_6": "",
            "custom_field_7": "",
            "comment": "",
            "created_at": "2020-07-28 14:54:39",
            "click_time": "2020-07-28 14:52:27",
            "referrer": "",
            "landing_id": 0,
            "prelanding_id": 0,
            "ref_id": "",
            "revenue": 32
        }
    ],
    "pagination": {
        "total_count": 1,
        "per_page": 100,
        "page": 1
    },
    "statusCode": 200
}

Можно увидеть, что ключ "clickid" отсутствует в ответе.
