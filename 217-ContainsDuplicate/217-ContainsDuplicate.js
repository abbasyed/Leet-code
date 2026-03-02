// Last updated: 3/1/2026, 11:44:38 PM
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const result = new Set();
    const seen = new Set();

    for ( let x of nums){
        if (seen.has(x)){
            return true
        }else{
            seen.add(x)
        }
    }return false
};