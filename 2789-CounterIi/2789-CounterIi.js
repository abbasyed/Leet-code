// Last updated: 9/14/2025, 4:58:46 AM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let current  = init
    const increment = () => {
        return current += 1
    }
    const decrement = () => {
        return current -= 1
    }
    const reset = () => {
        return current = init
    }
    return { increment, decrement, reset };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */