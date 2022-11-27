# ku_talai_api

KuTalaiApi - JavaScript client for ku_talai_api
To be added
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install ku_talai_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your ku_talai_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var KuTalaiApi = require('ku_talai_api');


var api = new KuTalaiApi.DefaultApi()
var busId = 56; // {Number} 
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.controllerGetBusRoute(busId, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8080/talai-api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*KuTalaiApi.DefaultApi* | [**controllerGetBusRoute**](docs/DefaultApi.md#controllerGetBusRoute) | **GET** /route/{busId} | Returns all bus stops for given route
*KuTalaiApi.DefaultApi* | [**controllerGetBuses**](docs/DefaultApi.md#controllerGetBuses) | **GET** /buses | Returns all KU Talai bus number
*KuTalaiApi.DefaultApi* | [**controllerGetBusstop**](docs/DefaultApi.md#controllerGetBusstop) | **GET** /busstop/{stopId} | Returns complete details of the specified Talai bus stop
*KuTalaiApi.DefaultApi* | [**controllerGetBusstopWeather**](docs/DefaultApi.md#controllerGetBusstopWeather) | **GET** /busstop/{stopId}/weather | Returns weather detail of the specified Talai bus stop
*KuTalaiApi.DefaultApi* | [**controllerGetBusstops**](docs/DefaultApi.md#controllerGetBusstops) | **GET** /busstops | Returns list of Talai bus stops in KU
*KuTalaiApi.DefaultApi* | [**controllerGetPopulation**](docs/DefaultApi.md#controllerGetPopulation) | **GET** /population/{stopId} | Get population density in each KU Talai bus
*KuTalaiApi.DefaultApi* | [**controllerGetRoutes**](docs/DefaultApi.md#controllerGetRoutes) | **GET** /routes | Returns a list of routes of KU Talai bus
*KuTalaiApi.DefaultApi* | [**controllerGetTakableBus**](docs/DefaultApi.md#controllerGetTakableBus) | **GET** /bus/{stopIdOrigin}/{stopIdDest} | Returns list of takable bus from origin to destination
*KuTalaiApi.DefaultApi* | [**controllerPutPopulation**](docs/DefaultApi.md#controllerPutPopulation) | **PUT** /population/{stopId} | Increment people in KU Talai bus stop


## Documentation for Models

 - [KuTalaiApi.Bus](docs/Bus.md)
 - [KuTalaiApi.Busstop](docs/Busstop.md)
 - [KuTalaiApi.BusstopWeather](docs/BusstopWeather.md)
 - [KuTalaiApi.Route](docs/Route.md)


## Documentation for Authorization

All endpoints do not require authorization.