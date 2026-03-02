// Last updated: 3/1/2026, 11:44:50 PM
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a,b) => a[0] - b[0])
    const result = [intervals[0]]

    for (let i = 1; i < intervals.length; i++){
        let last = result[result.length - 1]
        if(intervals[i][0] <= last[1]){
            last[1] = Math.max(last[1], intervals[i][1])
        }else{
            result.push(intervals[i])
        }
    }return result
};