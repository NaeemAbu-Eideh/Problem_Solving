/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    i = 0;
    for( j = 0; j < nums1.length; j++){
        if(nums1[j] == 0){
            if(i < nums2.length){
                nums1[j] = nums2[i];
                i++;
            }
        }
    }
    i = 0;
    for(;i < nums1.length; i++){
        for(j = 0; j < nums1.length; j++){
            if(nums1[i] < nums1[j]){
                [nums1[i], nums1[j]] = [nums1[j], nums1[i]];
            }
        }
    }
    return nums1;
};