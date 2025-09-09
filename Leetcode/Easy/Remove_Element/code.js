/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    for(let i = 0; i < nums.length;){
        if(nums[i] != val){i++;}
        else{
            nums.splice(i, 1);
        }
    }

    return nums.length;
};