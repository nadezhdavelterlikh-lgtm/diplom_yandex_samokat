# Вельтерлих Надежда, 35-я когорта - Финальный проект. Инженер потестированию плюс

import requests
import data
import configuration

# Создание заказа
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# Получение заказа по номеру трекера
def get_order_info_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track_number))
# Автотест
def test_get_order_info_by_track():
    track = create_order(data.order_body).json()['track']
    response = get_order_info_by_track(track)
    assert response.status_code == 200