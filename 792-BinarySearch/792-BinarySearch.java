// Last updated: 9/14/2025, 4:58:55 AM
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