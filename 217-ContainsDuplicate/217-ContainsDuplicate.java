// Last updated: 9/14/2025, 4:59:06 AM
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> res= new HashSet<>();

        for(int num: nums){
            if(res.contains(num)){
                return true;
            }
            res.add(num);
        }return false;
    }
}