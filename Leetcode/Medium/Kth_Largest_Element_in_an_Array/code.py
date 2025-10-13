/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

var findKthLargest = function(nums, k) {
    let swap = 0;
    nums =  nums.sort((a,b) => b - a);
    return nums[k-1];
};