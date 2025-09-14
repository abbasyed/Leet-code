// Last updated: 9/14/2025, 4:58:44 AM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const obj = {}
    obj.toBe  = function(compareVal) {
        if(val === compareVal){
            return true
        }
        throw new Error("Not Equal")
    }
    obj.notToBe = function(compareVal) {
        if(val !== compareVal){
            return true
        }
        throw new Error("Equal")
    }
    return obj
};
 