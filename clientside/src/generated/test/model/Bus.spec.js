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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.KuTalaiApi);
  }
}(this, function(expect, KuTalaiApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new KuTalaiApi.Bus();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Bus', function() {
    it('should create an instance of Bus', function() {
      // uncomment below and update the code to test Bus
      //var instance = new KuTalaiApi.Bus();
      //expect(instance).to.be.a(KuTalaiApi.Bus);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new KuTalaiApi.Bus();
      //expect(instance).to.be();
    });

    it('should have the property busNumber (base name: "bus_number")', function() {
      // uncomment below and update the code to test the property busNumber
      //var instance = new KuTalaiApi.Bus();
      //expect(instance).to.be();
    });

    it('should have the property busStopId (base name: "bus_stop_id")', function() {
      // uncomment below and update the code to test the property busStopId
      //var instance = new KuTalaiApi.Bus();
      //expect(instance).to.be();
    });

    it('should have the property routeId (base name: "route_id")', function() {
      // uncomment below and update the code to test the property routeId
      //var instance = new KuTalaiApi.Bus();
      //expect(instance).to.be();
    });

  });

}));
