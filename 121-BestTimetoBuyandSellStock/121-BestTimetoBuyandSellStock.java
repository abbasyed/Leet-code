// Last updated: 5/7/2025, 11:51:42 PM
class Solution {
    public int search(int[] nums, int target) {
        
        int low = 0; int right = nums.length-1;
        
        while (low <= right){
            int mid = low + (right - low) / 2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                right = mid - 1;
            }else{
                low = mid + 1;
            }
        }return -1;
    }
}