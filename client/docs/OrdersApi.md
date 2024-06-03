# swagger_client.OrdersApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_create_post**](OrdersApi.md#order_create_post) | **POST** /order/create | Создать заказ на товар
[**order_get**](OrdersApi.md#order_get) | **GET** /order | Получить список всех заказов
[**order_order_id_get**](OrdersApi.md#order_order_id_get) | **GET** /order/{order_id} | Получить информацию о заказе по его ID

# **order_create_post**
> order_create_post(body)

Создать заказ на товар

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
body = swagger_client.Order() # Order | 

try:
    # Создать заказ на товар
    api_instance.order_create_post(body)
except ApiException as e:
    print("Exception when calling OrdersApi->order_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Order**](Order.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get**
> list[Order] order_get()

Получить список всех заказов

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()

try:
    # Получить список всех заказов
    api_response = api_instance.order_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Order]**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_order_id_get**
> Order order_order_id_get(order_id)

Получить информацию о заказе по его ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order_id = 789 # int | 

try:
    # Получить информацию о заказе по его ID
    api_response = api_instance.order_order_id_get(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->order_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

