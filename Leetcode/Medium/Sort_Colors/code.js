/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(i = 0; i < nums.length; i++){
        for(j = 0; j < nums.length; j++){
            if(nums[i] < nums[j]){
                swap = nums[i];
                nums[i] = nums[j];
                nums[j] = swap;
            }
        }
    }
    return nums;
};