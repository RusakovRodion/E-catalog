import connexion
import six

from swagger_server.models.category import Category  # noqa: E501
from swagger_server import util


def category_get():  # noqa: E501
    """Получить список всех категорий

     # noqa: E501


    :rtype: List[Category]
    """
    return 'do some magic!'


def category_post(body):  # noqa: E501
    """Добавить новую категорию

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Category.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
