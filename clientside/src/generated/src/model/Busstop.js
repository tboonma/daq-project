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
 * The Busstop model module.
 * @module model/Busstop
 * @version 1.0.0
 */
class Busstop {
    /**
     * Constructs a new <code>Busstop</code>.
     * @alias module:model/Busstop
     */
    constructor() { 
        
        Busstop.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Busstop</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Busstop} obj Optional instance to populate.
     * @return {module:model/Busstop} The populated <code>Busstop</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Busstop();

            if (data.hasOwnProperty('busstopId')) {
                obj['busstopId'] = ApiClient.convertToType(data['busstopId'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('lat')) {
                obj['lat'] = ApiClient.convertToType(data['lat'], 'Number');
            }
            if (data.hasOwnProperty('lon')) {
                obj['lon'] = ApiClient.convertToType(data['lon'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Busstop</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Busstop</code>.
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
 * @member {Number} busstopId
 */
Busstop.prototype['busstopId'] = undefined;

/**
 * @member {String} name
 */
Busstop.prototype['name'] = undefined;

/**
 * @member {Number} lat
 */
Busstop.prototype['lat'] = undefined;

/**
 * @member {Number} lon
 */
Busstop.prototype['lon'] = undefined;






export default Busstop;
