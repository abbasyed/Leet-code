class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #initialize empty dictionary/hashmap for storing value and index positions
        resultMap = {}
        #interate through the loop by index and value for the nums array
        for index, val in enumerate(nums):
            #if val appears in resultMap return true
            if val in resultMap:
                return True
            else:
                #add value and index to resultMap dictionary
                resultMap[val] = index
        #if value doesn't appear in the hashmap return false        
        return False
