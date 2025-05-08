// Last updated: 5/7/2025, 8:33:22 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        int uniqueIndex = 1;
        for (int i = 1; i < nums.length; i++){
            if(nums[i] != nums[uniqueIndex-1]){
                nums[uniqueIndex++] = nums[i]; 
            }
        }return uniqueIndex;
    }
}