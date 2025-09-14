// Last updated: 9/14/2025, 4:59:00 AM
class Solution {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length- 1;

        while (left < right){
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}