// Last updated: 3/1/2026, 11:44:45 PM
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity
    let maxProfit = 0
    for (let num of prices){
        if(num < minPrice){
            minPrice = num
        }
         let profit = num - minPrice
        if(profit > maxProfit){
            maxProfit = profit
        }
    }return maxProfit
    
};