/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    arr2 = [];
    for(i = 0; i < arr.length; i++){
        check = fn(arr[i], i);
        if(typeof check == "boolean"){
            if(check == true){
            arr2.push(arr[i]);
            }
        }
        else{
            num = fn(arr[i], i);
            if(num != 0){
                arr2.push(arr[i]);
            }
        }
    
    }
    return arr2;
};