# market_client.OrdersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_request**](OrdersApi.md#get_order_request) | **GET** /openapi/v2/orders/{orderID} | get order infos


# **get_order_request**
> AppListResponse get_order_request(order_id)

get order infos

Gets the specified order information

### Example
```python
from __future__ import print_function
import time
import market_client
from market_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: enterprise_key
configuration = market_client.Configuration()
configuration.api_key['X_ENTERPRISE_ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X_ENTERPRISE_ID'] = 'Bearer'
# Configure API key authorization: token_key
configuration = market_client.Configuration()
configuration.api_key['X_ENTERPRISE_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X_ENTERPRISE_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = market_client.OrdersApi(market_client.ApiClient(configuration))
order_id = 789 # int | an id of order

try:
    # get order infos
    api_response = api_instance.get_order_request(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| an id of order | 

### Return type

[**AppListResponse**](AppListResponse.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

