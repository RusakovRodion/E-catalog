# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_order_create_post(self):
        """Test case for order_create_post

        Создать заказ на товар
        """
        body = Order()
        response = self.client.open(
            '/api/v1/order/create',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_get(self):
        """Test case for order_get

        Получить список всех заказов
        """
        response = self.client.open(
            '/api/v1/order',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_order_order_id_get(self):
        """Test case for order_order_id_get

        Получить информацию о заказе по его ID
        """
        response = self.client.open(
            '/api/v1/order/{order_id}'.format(order_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
