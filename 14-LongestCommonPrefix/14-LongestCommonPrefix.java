// Last updated: 5/6/2025, 12:30:04 AM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if( strs == null || strs.length == 0) return "";

        String prefix = strs[0];
        for (String s: strs){
            while(!s.startsWith(prefix)){
                prefix = prefix.substring(0, prefix.length()-1);
                if(prefix.isEmpty()) return "";
            }
        }return prefix;
    }
}