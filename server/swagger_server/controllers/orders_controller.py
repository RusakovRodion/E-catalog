import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


def order_create_post(body):  # noqa: E501
    """Создать заказ на товар

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def order_get():  # noqa: E501
    """Получить список всех заказов

     # noqa: E501


    :rtype: List[Order]
    """
    return 'do some magic!'


def order_order_id_get(order_id):  # noqa: E501
    """Получить информацию о заказе по его ID

     # noqa: E501

    :param order_id: 
    :type order_id: int

    :rtype: Order
    """
    return 'do some magic!'
