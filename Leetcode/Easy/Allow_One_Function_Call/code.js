/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    i = 0;

    return function(...args){
        if(i == 0){
            val = fn(...args);
            i++;
            return val;
        }
        else{
            return undefined;
        }
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
