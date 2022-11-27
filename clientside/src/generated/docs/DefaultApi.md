# KuTalaiApi.DefaultApi

All URIs are relative to *http://127.0.0.1:8080/talai-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllerGetBusRoute**](DefaultApi.md#controllerGetBusRoute) | **GET** /route/{busId} | Returns all bus stops for given route
[**controllerGetBuses**](DefaultApi.md#controllerGetBuses) | **GET** /buses | Returns all KU Talai bus number
[**controllerGetBusstop**](DefaultApi.md#controllerGetBusstop) | **GET** /busstop/{stopId} | Returns complete details of the specified Talai bus stop
[**controllerGetBusstopWeather**](DefaultApi.md#controllerGetBusstopWeather) | **GET** /busstop/{stopId}/weather | Returns weather detail of the specified Talai bus stop
[**controllerGetBusstops**](DefaultApi.md#controllerGetBusstops) | **GET** /busstops | Returns list of Talai bus stops in KU
[**controllerGetPopulation**](DefaultApi.md#controllerGetPopulation) | **GET** /population/{stopId} | Get population density in each KU Talai bus
[**controllerGetRoutes**](DefaultApi.md#controllerGetRoutes) | **GET** /routes | Returns a list of routes of KU Talai bus
[**controllerGetTakableBus**](DefaultApi.md#controllerGetTakableBus) | **GET** /bus/{stopIdOrigin}/{stopIdDest} | Returns list of takable bus from origin to destination
[**controllerPutPopulation**](DefaultApi.md#controllerPutPopulation) | **PUT** /population/{stopId} | Increment people in KU Talai bus stop



## controllerGetBusRoute

> controllerGetBusRoute(busId)

Returns all bus stops for given route

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
let busId = 56; // Number | 
apiInstance.controllerGetBusRoute(busId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## controllerGetBuses

> controllerGetBuses()

Returns all KU Talai bus number

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
apiInstance.controllerGetBuses((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## controllerGetBusstop

> Busstop controllerGetBusstop(stopId)

Returns complete details of the specified Talai bus stop

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
let stopId = 56; // Number | 
apiInstance.controllerGetBusstop(stopId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopId** | **Number**|  | 

### Return type

[**Busstop**](Busstop.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllerGetBusstopWeather

> BusstopWeather controllerGetBusstopWeather(stopId)

Returns weather detail of the specified Talai bus stop

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
let stopId = 56; // Number | 
apiInstance.controllerGetBusstopWeather(stopId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopId** | **Number**|  | 

### Return type

[**BusstopWeather**](BusstopWeather.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllerGetBusstops

> [Busstop] controllerGetBusstops()

Returns list of Talai bus stops in KU

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
apiInstance.controllerGetBusstops((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Busstop]**](Busstop.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllerGetPopulation

> controllerGetPopulation(stopId)

Get population density in each KU Talai bus

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
let stopId = 56; // Number | 
apiInstance.controllerGetPopulation(stopId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## controllerGetRoutes

> [Route] controllerGetRoutes()

Returns a list of routes of KU Talai bus

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
apiInstance.controllerGetRoutes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Route]**](Route.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## controllerGetTakableBus

> controllerGetTakableBus(stopIdOrigin, stopIdDest)

Returns list of takable bus from origin to destination

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
let stopIdOrigin = 56; // Number | 
let stopIdDest = 56; // Number | 
apiInstance.controllerGetTakableBus(stopIdOrigin, stopIdDest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopIdOrigin** | **Number**|  | 
 **stopIdDest** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## controllerPutPopulation

> controllerPutPopulation(stopId)

Increment people in KU Talai bus stop

### Example

```javascript
import KuTalaiApi from 'ku_talai_api';

let apiInstance = new KuTalaiApi.DefaultApi();
let stopId = 56; // Number | 
apiInstance.controllerPutPopulation(stopId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stopId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined
