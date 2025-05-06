// Last updated: 5/6/2025, 4:30:35 PM
class Solution {
    public void moveZeroes(int[] nums) {

        int index = 0;

        for (int n: nums){
            if(n != 0){
                nums[index++] = n;
            }
        
        }while(index < nums.length){
            nums[index++] = 0;
        }
        
    }
}