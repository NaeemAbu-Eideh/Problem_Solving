/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void}
 */
var rotate = function(nums, k) {
    const n = nums.length;
    k = k % n; 
    let temp = [];

    for (let i = n - k; i < n; i++) {
        temp.push(nums[i]);
    }

    for (let i = 0; i < n - k; i++) {
        temp.push(nums[i]);
    }

    for (let i = 0; i < n; i++) {
        nums[i] = temp[i];
    }
};