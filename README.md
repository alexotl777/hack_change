## Архитектура API:
- `GET /documents/deque_bids/{product}/{status}` Отдает все сделки по статусу и продукту кредитования, отсортированные по дате создания.
- `GET/documents/bid/{id}` Возвращает данные о сделке, только всю инфу. (1 метод номер возвращает и сумму)
- `GET/participants/{id}` Возвращает данные участника сделки _(как в анкете)_
- `GET documents/bid/{id}/docs` скачивает архив с документами участника
___
## Scripts
_Папка с логикой вычисления рисков_
#### level_risk
Высчитывает уровень риска по таблице (Приложение 5)

#### pdn
Высчитывает ПДН клиента по формуле ПДН = 'сумма среднемесячных платежей по всем кредитам и займам заемщика' ДЕЛИТЬ на 'величина среднемесячного дохода заемщика' * 100%
Существуют риски в случае, если рассчитанное значение ПДН заемщика превышает 50%
Источник - https://cbr.ru/finstab/instruments/pti/

### risks_of_trade
Функции для 4ого пункта. Описание рисков по сделке (Автоматическая проверка, заглушки)
___
## Салют
Асистент может использоваться для оценки рисков, для запроса информации, перевода на оператора
___
## Макет интерфейса
_Ссылка на миро_:
https://miro.com/welcomeonboard/eHJWVzJmeTcyd2ZZc01tUGF1UkREVktpR1lmUXAxUW81UkRJaUNHV2ZCR0xrTGw0akhEQnRFUktkWVh3ejhkNHwzNDU4NzY0NTY3NzYwMTYyODYyfDI=?share_link_id=216211349724
___
## Запуск сервера
Для запуска сервера выполните команду в терминале из корневой папки проекта:
```bash
python3 main.py
```