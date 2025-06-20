"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=0
        for i in range(0,len(nums)):
            if(nums[i]==val):
                continue
            else:
                nums[count]=nums[i]
                count=count+1

        return count
    
sol = Solution()
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = sol.removeElement(nums1, val1)
print(k1, nums1[:k1])

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
k2 = sol.removeElement(nums2, val2)
print(k2, nums2[:k2])

nums3 = [1,1,1,1]
val3 = 1
k3 = sol.removeElement(nums3, val3)
print(k3, nums3[:k3])

nums4 = []
val4 = 0
k4 = sol.removeElement(nums4, val4)
print(k4, nums4[:k4])

nums5 = [4,5]
val5 = 6
k5 = sol.removeElement(nums5, val5)
print(k5, nums5[:k5])
