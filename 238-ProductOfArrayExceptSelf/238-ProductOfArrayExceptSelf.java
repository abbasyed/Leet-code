// Last updated: 9/14/2025, 4:59:03 AM
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