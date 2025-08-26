class Solution(object):
    def longestSubarray(self, nums):
        left, right = 0, 0     
        indicator = False      
        max_len = 0

        for x in nums:
            if x == 1:
                right += 1
            else:
                indicator = True
                left = right   
                right = 0      
            if left + right > max_len:
                max_len = left + right

        if not indicator:
            return len(nums) - 1
        return max_len
