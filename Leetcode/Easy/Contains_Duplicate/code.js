/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let seen = new Set();
    for(let char of nums){
        if(seen.has(char)) return true;
        seen.add(char);
    }
    return false;
};