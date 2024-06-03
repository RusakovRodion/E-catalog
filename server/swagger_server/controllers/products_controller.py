import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def products_get():  # noqa: E501
    """Получить список всех товаров

     # noqa: E501


    :rtype: List[Product]
    """
    return 'do some magic!'


def products_post(body):  # noqa: E501
    """Добавить товар

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def products_product_id_delete(product_id):  # noqa: E501
    """Удалить товар по ID

     # noqa: E501

    :param product_id: 
    :type product_id: int

    :rtype: None
    """
    return 'do some magic!'


def products_product_id_get(product_id):  # noqa: E501
    """Получить информацию о товаре по ID

     # noqa: E501

    :param product_id: 
    :type product_id: int

    :rtype: Product
    """
    return 'do some magic!'


def products_product_id_put(body, product_id):  # noqa: E501
    """Изменить информацию о товаре по ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param product_id: 
    :type product_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
