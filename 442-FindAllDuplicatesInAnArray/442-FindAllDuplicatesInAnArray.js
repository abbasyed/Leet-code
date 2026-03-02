// Last updated: 3/1/2026, 11:44:27 PM
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {

    const seen = new Set()
    const result = new Set()

    for (let num of nums){
        if(seen.has(num)){
            result.add(num)
        }
        else{
            seen.add(num)
        }
    }   return[...result]
    
};