// Last updated: 5/7/2025, 11:27:49 PM
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] res = new int[nums.length];

        int prefix = 1;
        for (int i=0; i<nums.length; i++){
            res[i] = prefix;
            prefix *= nums[i];
        }
        int suffix = 1;
        for (int i = nums.length -1; i >= 0; i--){
            res[i] *= suffix;
            suffix *= nums[i];
        }return res;
    }
}