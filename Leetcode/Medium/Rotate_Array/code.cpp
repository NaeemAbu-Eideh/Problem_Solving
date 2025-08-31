class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> num1;

        if (nums.size() <= 1) return;

        k = k % nums.size();

        if (k == 0) return;

        for (int i = nums.size() - k; i < nums.size(); i++) {
            num1.push_back(nums[i]);
        }

        for (int i = 0; i < nums.size() - k; i++) {
            num1.push_back(nums[i]);
        }

        nums = num1;
    }
};