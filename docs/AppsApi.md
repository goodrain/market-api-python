# market_client.AppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_version**](AppsApi.md#create_app_version) | **POST** /openapi/v2/markets/{marketID}/apps/{appID}/versions | 
[**creeate_enterprise_market_app**](AppsApi.md#creeate_enterprise_market_app) | **POST** /openapi/v2/markets/{marketID}/apps | 
[**download_app_by_order**](AppsApi.md#download_app_by_order) | **GET** /openapi/v2/orders/{orderID}/downloadapp | 
[**get_app_version**](AppsApi.md#get_app_version) | **GET** /openapi/v2/markets/{marketID}/apps/{appID}/versions/{versionID} | 
[**get_app_versions**](AppsApi.md#get_app_versions) | **GET** /openapi/v2/markets/{marketID}/apps/{appID}/versions | 
[**get_enterprise_market_app_and_version**](AppsApi.md#get_enterprise_market_app_and_version) | **GET** /openapi/v2/markets/{marketID}/apps/{appID} | 
[**get_enterprise_market_apps_and_versions**](AppsApi.md#get_enterprise_market_apps_and_versions) | **GET** /openapi/v2/markets/{marketID}/apps | 
[**get_enterprise_market_by_market_id**](AppsApi.md#get_enterprise_market_by_market_id) | **GET** /openapi/v2/markets/{marketID} | 
[**get_recommended_app_list**](AppsApi.md#get_recommended_app_list) | **GET** /openapi/v2/recommended/apps | get recommended app list


# **create_app_version**
> StoreAppVersion create_app_version()



create app version

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.create_app_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->create_app_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoreAppVersion**](StoreAppVersion.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, Schemes:

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **creeate_enterprise_market_app**
> ResponseData creeate_enterprise_market_app()



create app

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.creeate_enterprise_market_app()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->creeate_enterprise_market_app: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResponseData**](ResponseData.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, Schemes:

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_app_by_order**
> StoreAppVersion download_app_by_order(order_id)



download app installation metadata by order

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))
order_id = 789 # int | an id of order

try:
    api_response = api_instance.download_app_by_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->download_app_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| an id of order | 

### Return type

[**StoreAppVersion**](StoreAppVersion.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_version**
> StoreAppVersion get_app_version()



get app specify version

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.get_app_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_app_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoreAppVersion**](StoreAppVersion.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, Schemes:

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_versions**
> StoreAppVersion get_app_versions()



get app all versions

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.get_app_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_app_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoreAppVersion**](StoreAppVersion.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprise_market_app_and_version**
> StoreApp get_enterprise_market_app_and_version()



get app

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.get_enterprise_market_app_and_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_enterprise_market_app_and_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoreApp**](StoreApp.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, Schemes:

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprise_market_apps_and_versions**
> AppListResponse get_enterprise_market_apps_and_versions()



get app list

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.get_enterprise_market_apps_and_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_enterprise_market_apps_and_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppListResponse**](AppListResponse.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, Schemes:

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprise_market_by_market_id**
> Market get_enterprise_market_by_market_id()



get market

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))

try:
    api_response = api_instance.get_enterprise_market_by_market_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_enterprise_market_by_market_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Market**](Market.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, Schemes:

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recommended_app_list**
> AppListResponse get_recommended_app_list(page=page, limit=limit, group_name=group_name)

get recommended app list

This will show recommended app

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
api_instance = market_client.AppsApi(market_client.ApiClient(configuration))
page = 789 # int | current page number (optional)
limit = 789 # int | current page limit number (optional)
group_name = 789 # int | search for application name (optional)

try:
    # get recommended app list
    api_response = api_instance.get_recommended_app_list(page=page, limit=limit, group_name=group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_recommended_app_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| current page number | [optional] 
 **limit** | **int**| current page limit number | [optional] 
 **group_name** | **int**| search for application name | [optional] 

### Return type

[**AppListResponse**](AppListResponse.md)

### Authorization

[enterprise_key](../README.md#enterprise_key), [token_key](../README.md#token_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

