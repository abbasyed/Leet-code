// Last updated: 5/7/2025, 11:22:08 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        // base case:
        if(strs.length == 0 || strs == null) return "";

        String prefix = strs[0];
        for(String s: strs){
            while(!s.startsWith(prefix)){
                prefix = prefix.substring(0, prefix.length()-1);
                if(prefix.isEmpty()) return "";
            }
        }return prefix;
    }
}