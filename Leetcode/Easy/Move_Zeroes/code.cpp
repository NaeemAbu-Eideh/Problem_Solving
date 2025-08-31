class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> num1;
        for(int i=0;i<nums.size();i++){
            if(nums[i] != 0){
                num1.push_back(nums[i]);
            }
        }
        for(int i=0;i<nums.size();i++){
            if(nums[i] == 0){
                num1.push_back(nums[i]);
            }
        }
        nums = num1;
    }
};