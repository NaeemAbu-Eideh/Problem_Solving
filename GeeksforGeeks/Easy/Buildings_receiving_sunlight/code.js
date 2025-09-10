// User function Template for javascript
/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    
    longest(arr) {
        let count = 0;
        let target = arr[0];
        for(let i = 1 ; i < arr.length;i++){
            if(target > arr[i]){count++}
            else{
                target = arr[i];
            }
        }
        let result = arr.length - count;
        return result;
    }
}