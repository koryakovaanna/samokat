import configuration
import requests
import data


# Функция для запроса создания заказа
def create_order(body):
    return requests.post(f'{configuration.DOMAIN}{configuration.ORDER_CREATE_PATH}', json=body, headers=data.headers)


# Функция для получения информации о заказе по его трек номеру
def get_tracking_info(track_id):
    request_path = f'{configuration.DOMAIN}{configuration.GET_TRACK_INFO_PATH}'
    return requests.get(request_path,
                        params={'t': track_id},
                        headers=data.headers
                        )
