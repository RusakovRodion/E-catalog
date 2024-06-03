from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import logging

#Логгер
logging.basicConfig(filename="../server/var/log/temp.log", level=logging.INFO)

# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://192.168.20.217:8080/api/v1'
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))

while(True):
    time.sleep(1)
    try:
        # Получить список всех категорий
        api_response = api_instance.category_get()
        pprint(api_response)
        logging.info("Get list of Categories successfully")
    except ApiException as e:
        print("Exception when calling CategoriesApi->category_get: %s\n" % e)
        logging.info("Exception when calling CategoriesApi->category_get: %s\n" % e)

    # create an instance of the API class
    api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
    body = swagger_client.Category() # Category |

    try:
        # Добавить новую категорию
        api_instance.category_post(body)
        logging.info("New Category added successfully")
    except ApiException as e:
        print("Exception when calling CategoriesApi->category_post: %s\n" % e)
        logging.info("Exception when calling CategoriesApi->category_post: %s\n" % e)