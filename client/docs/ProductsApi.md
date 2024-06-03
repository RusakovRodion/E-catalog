# swagger_client.ProductsApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_get**](ProductsApi.md#products_get) | **GET** /products | Получить список всех товаров
[**products_post**](ProductsApi.md#products_post) | **POST** /products | Добавить товар
[**products_product_id_delete**](ProductsApi.md#products_product_id_delete) | **DELETE** /products/{product_id} | Удалить товар по ID
[**products_product_id_get**](ProductsApi.md#products_product_id_get) | **GET** /products/{product_id} | Получить информацию о товаре по ID
[**products_product_id_put**](ProductsApi.md#products_product_id_put) | **PUT** /products/{product_id} | Изменить информацию о товаре по ID

# **products_get**
> list[Product] products_get()

Получить список всех товаров

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try:
    # Получить список всех товаров
    api_response = api_instance.products_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_post**
> products_post(body)

Добавить товар

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
body = swagger_client.Product() # Product | 

try:
    # Добавить товар
    api_instance.products_post(body)
except ApiException as e:
    print("Exception when calling ProductsApi->products_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_delete**
> products_product_id_delete(product_id)

Удалить товар по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
product_id = 789 # int | 

try:
    # Удалить товар по ID
    api_instance.products_product_id_delete(product_id)
except ApiException as e:
    print("Exception when calling ProductsApi->products_product_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_get**
> Product products_product_id_get(product_id)

Получить информацию о товаре по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
product_id = 789 # int | 

try:
    # Получить информацию о товаре по ID
    api_response = api_instance.products_product_id_get(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_product_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_put**
> products_product_id_put(body, product_id)

Изменить информацию о товаре по ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
body = swagger_client.Product() # Product | 
product_id = 789 # int | 

try:
    # Изменить информацию о товаре по ID
    api_instance.products_product_id_put(body, product_id)
except ApiException as e:
    print("Exception when calling ProductsApi->products_product_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | 
 **product_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

