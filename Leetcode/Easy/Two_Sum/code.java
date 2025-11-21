class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            int num = target - nums[i];
            if(map.containsKey(num)){
                int [] arr = new int[2];
                arr[0] = map.get(num);
                arr[1] = i;
                return arr;
            }
            map.put(nums[i], i);
        }
        int []arr = new int[2];
        return arr;
    }
}

