// Last updated: 3/1/2026, 11:45:01 PM
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const map = {
        "}":"{",
        ")":"(",
        "]":"["
    }
    const stack = []
    for (let x of s){
        if(!(x in map)){
            stack.push(x)
        }
        else{
            const top = stack.pop(x)
            if(top === map[x]){
                continue
            }
            else{
                return false
            }
        }
    }return stack.length === 0;
};