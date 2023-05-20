import sender_stand_request
import data


# Ф-я тестирования создания заказа и его доступности по трек номеру
def test_check_tracking_info_recieved_after_order_creation():
    create_order_response = sender_stand_request.create_order(data.order_create_body)
    assert create_order_response.status_code == 201
    create_order_response_json = create_order_response.json()
    track_id = create_order_response_json['track']
    # Проверяем что track приходит
    assert track_id >= 0
    get_track_response = sender_stand_request.get_tracking_info(track_id)
    # Проверяем что информация о заказе по треку приходит
    assert get_track_response.status_code == 200
