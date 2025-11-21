/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    arr2 = [];
    for(i = 0; i < arr.length; i++){
        arr2.push(fn(arr[i], i));
    }
    return arr2;
};