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

import ApiClient from '../ApiClient';

/**
 * The Route model module.
 * @module model/Route
 * @version 1.0.0
 */
class Route {
    /**
     * Constructs a new <code>Route</code>.
     * @alias module:model/Route
     */
    constructor() { 
        
        Route.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Route</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Route} obj Optional instance to populate.
     * @return {module:model/Route} The populated <code>Route</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Route();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('routeNumber')) {
                obj['routeNumber'] = ApiClient.convertToType(data['routeNumber'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Route</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Route</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {Number} id
 */
Route.prototype['id'] = undefined;

/**
 * @member {Number} routeNumber
 */
Route.prototype['routeNumber'] = undefined;

/**
 * @member {String} name
 */
Route.prototype['name'] = undefined;






export default Route;
