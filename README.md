# rainbond-market-client
the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 0.0.4
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.rainbond.com](https://www.rainbond.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import market_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import market_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppsApi* | [**download_app_by_order**](docs/AppsApi.md#download_app_by_order) | **GET** /openapi/v2/orders/{orderID}/downloadapp | 
*AppsApi* | [**get_recommended_app_list**](docs/AppsApi.md#get_recommended_app_list) | **GET** /openapi/v2/recommended/apps | get recommended app list
*OrdersApi* | [**get_order_request**](docs/OrdersApi.md#get_order_request) | **GET** /openapi/v2/orders/{orderID} | get order infos


## Documentation For Models

 - [AppListResponse](docs/AppListResponse.md)
 - [DeployType](docs/DeployType.md)
 - [Enterprise](docs/Enterprise.md)
 - [ImageInfo](docs/ImageInfo.md)
 - [Order](docs/Order.md)
 - [OrderApp](docs/OrderApp.md)
 - [OrderInfoResponse](docs/OrderInfoResponse.md)
 - [OrderState](docs/OrderState.md)
 - [OrderSvcProvider](docs/OrderSvcProvider.md)
 - [StoreApp](docs/StoreApp.md)
 - [StoreAppTag](docs/StoreAppTag.md)
 - [StoreAppVersion](docs/StoreAppVersion.md)
 - [StoreAppVersionTemplete](docs/StoreAppVersionTemplete.md)
 - [StoreAppVersionTempleteApp](docs/StoreAppVersionTempleteApp.md)
 - [StoreAppVersionTempleteAppDepService](docs/StoreAppVersionTempleteAppDepService.md)
 - [StoreAppVersionTempleteAppEnv](docs/StoreAppVersionTempleteAppEnv.md)
 - [StoreAppVersionTempleteAppExtendMethodRule](docs/StoreAppVersionTempleteAppExtendMethodRule.md)
 - [StoreAppVersionTempleteAppPluginConfig](docs/StoreAppVersionTempleteAppPluginConfig.md)
 - [StoreAppVersionTempleteAppPort](docs/StoreAppVersionTempleteAppPort.md)
 - [StoreAppVersionTempleteAppProbe](docs/StoreAppVersionTempleteAppProbe.md)
 - [StoreAppVersionTempleteAppShareVolume](docs/StoreAppVersionTempleteAppShareVolume.md)
 - [StoreAppVersionTempleteAppVolume](docs/StoreAppVersionTempleteAppVolume.md)
 - [StoreAppVersionTempleteAppVolumeList](docs/StoreAppVersionTempleteAppVolumeList.md)
 - [StoreAppVersionTempletePlugin](docs/StoreAppVersionTempletePlugin.md)
 - [StoreAppVersionTempletePluginConfigGroup](docs/StoreAppVersionTempletePluginConfigGroup.md)
 - [StoreAppVersionTempletePluginConfigGroupOption](docs/StoreAppVersionTempletePluginConfigGroupOption.md)
 - [TempleteVersion](docs/TempleteVersion.md)
 - [VolumeType](docs/VolumeType.md)


## Documentation For Authorization


## enterprise_key

- **Type**: API key
- **API key parameter name**: X_ENTERPRISE_ID
- **Location**: HTTP header

## token_key

- **Type**: API key
- **API key parameter name**: X_ENTERPRISE_TOKEN
- **Location**: HTTP header


## Author

576501057@qq.com
