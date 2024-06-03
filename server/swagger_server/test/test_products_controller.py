# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_products_get(self):
        """Test case for products_get

        Получить список всех товаров
        """
        response = self.client.open(
            '/api/v1/products',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_post(self):
        """Test case for products_post

        Добавить товар
        """
        body = Product()
        response = self.client.open(
            '/api/v1/products',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_delete(self):
        """Test case for products_product_id_delete

        Удалить товар по ID
        """
        response = self.client.open(
            '/api/v1/products/{product_id}'.format(product_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_get(self):
        """Test case for products_product_id_get

        Получить информацию о товаре по ID
        """
        response = self.client.open(
            '/api/v1/products/{product_id}'.format(product_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_put(self):
        """Test case for products_product_id_put

        Изменить информацию о товаре по ID
        """
        body = Product()
        response = self.client.open(
            '/api/v1/products/{product_id}'.format(product_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
