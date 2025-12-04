/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    i = 0; 
    j = 1;
    len = nums.length;
    while(j < len){
        if(nums[i] == nums[j]){
            nums.splice(j, 1);
            len--;
        }
        else{
            j++;
            i++;
        }
    }

    console.log(len);
};