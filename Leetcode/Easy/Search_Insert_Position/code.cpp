class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int targ = -1;
        for(int i = 0 ; i < nums.size(); i++){
            if(nums[i] == target) targ = i;
        }
        if(targ != -1){return targ;}
        else{
            int i = 0;
            for(; i < nums.size(); i++){
                if(target < nums[i]){targ = i;break;}
            }
            if(i == nums.size())return i;
            else return targ;
        }
    }
};