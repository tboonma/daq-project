/**
 * KU Talai API
 * To be added
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Busstop from '../model/Busstop';
import BusstopWeather from '../model/BusstopWeather';
import PopulationDensity from '../model/PopulationDensity';
import Route from '../model/Route';

/**
* Default service.
* @module api/DefaultApi
* @version 1.0.0
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the controllerGetBusRoute operation.
     * @callback module:api/DefaultApi~controllerGetBusRouteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns all bus stops for given route
     * @param {Number} busId 
     * @param {module:api/DefaultApi~controllerGetBusRouteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    controllerGetBusRoute(busId, callback) {
      let postBody = null;
      // verify the required parameter 'busId' is set
      if (busId === undefined || busId === null) {
        throw new Error("Missing the required parameter 'busId' when calling controllerGetBusRoute");
      }

      let pathParams = {
        'busId': busId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/route/{busId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetBuses operation.
     * @callback module:api/DefaultApi~controllerGetBusesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns all KU Talai bus number
     * @param {module:api/DefaultApi~controllerGetBusesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    controllerGetBuses(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/buses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetBusstop operation.
     * @callback module:api/DefaultApi~controllerGetBusstopCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Busstop} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns complete details of the specified Talai bus stop
     * @param {Number} stopId 
     * @param {module:api/DefaultApi~controllerGetBusstopCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Busstop}
     */
    controllerGetBusstop(stopId, callback) {
      let postBody = null;
      // verify the required parameter 'stopId' is set
      if (stopId === undefined || stopId === null) {
        throw new Error("Missing the required parameter 'stopId' when calling controllerGetBusstop");
      }

      let pathParams = {
        'stopId': stopId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Busstop;
      return this.apiClient.callApi(
        '/busstop/{stopId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetBusstopWeather operation.
     * @callback module:api/DefaultApi~controllerGetBusstopWeatherCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BusstopWeather} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns weather detail of the specified Talai bus stop
     * @param {Number} stopId 
     * @param {module:api/DefaultApi~controllerGetBusstopWeatherCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BusstopWeather}
     */
    controllerGetBusstopWeather(stopId, callback) {
      let postBody = null;
      // verify the required parameter 'stopId' is set
      if (stopId === undefined || stopId === null) {
        throw new Error("Missing the required parameter 'stopId' when calling controllerGetBusstopWeather");
      }

      let pathParams = {
        'stopId': stopId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BusstopWeather;
      return this.apiClient.callApi(
        '/busstop/{stopId}/weather', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetBusstops operation.
     * @callback module:api/DefaultApi~controllerGetBusstopsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Busstop>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns list of Talai bus stops in KU
     * @param {module:api/DefaultApi~controllerGetBusstopsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Busstop>}
     */
    controllerGetBusstops(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Busstop];
      return this.apiClient.callApi(
        '/busstops', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetPopulation operation.
     * @callback module:api/DefaultApi~controllerGetPopulationCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/PopulationDensity>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get population density in each KU Talai bus
     * @param {Number} stopId 
     * @param {module:api/DefaultApi~controllerGetPopulationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/PopulationDensity>}
     */
    controllerGetPopulation(stopId, callback) {
      let postBody = null;
      // verify the required parameter 'stopId' is set
      if (stopId === undefined || stopId === null) {
        throw new Error("Missing the required parameter 'stopId' when calling controllerGetPopulation");
      }

      let pathParams = {
        'stopId': stopId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [PopulationDensity];
      return this.apiClient.callApi(
        '/population/{stopId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetRoutes operation.
     * @callback module:api/DefaultApi~controllerGetRoutesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Route>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a list of routes of KU Talai bus
     * @param {module:api/DefaultApi~controllerGetRoutesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Route>}
     */
    controllerGetRoutes(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Route];
      return this.apiClient.callApi(
        '/routes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerGetTakableBus operation.
     * @callback module:api/DefaultApi~controllerGetTakableBusCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns list of takable bus from origin to destination
     * @param {Number} stopIdOrigin 
     * @param {Number} stopIdDest 
     * @param {module:api/DefaultApi~controllerGetTakableBusCallback} callback The callback function, accepting three arguments: error, data, response
     */
    controllerGetTakableBus(stopIdOrigin, stopIdDest, callback) {
      let postBody = null;
      // verify the required parameter 'stopIdOrigin' is set
      if (stopIdOrigin === undefined || stopIdOrigin === null) {
        throw new Error("Missing the required parameter 'stopIdOrigin' when calling controllerGetTakableBus");
      }
      // verify the required parameter 'stopIdDest' is set
      if (stopIdDest === undefined || stopIdDest === null) {
        throw new Error("Missing the required parameter 'stopIdDest' when calling controllerGetTakableBus");
      }

      let pathParams = {
        'stopIdOrigin': stopIdOrigin,
        'stopIdDest': stopIdDest
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/bus/{stopIdOrigin}/{stopIdDest}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the controllerPutPopulation operation.
     * @callback module:api/DefaultApi~controllerPutPopulationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Increment people in KU Talai bus stop
     * @param {Number} stopId 
     * @param {module:api/DefaultApi~controllerPutPopulationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    controllerPutPopulation(stopId, callback) {
      let postBody = null;
      // verify the required parameter 'stopId' is set
      if (stopId === undefined || stopId === null) {
        throw new Error("Missing the required parameter 'stopId' when calling controllerPutPopulation");
      }

      let pathParams = {
        'stopId': stopId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/population/{stopId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
