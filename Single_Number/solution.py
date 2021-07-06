# https://leetcode.com/problems/single-number/
# Faster than 84.52%
# Memory usage less than 99.81%
class Solution0:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums)!=1:
            nums[0]^=nums.pop()
        return nums[0]



# Faster than 97.90%
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer
      
      
      
# Faster than 97.90%
# Memory usage less than 99.81%
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        i = len(nums)
        while i!=1:
            nums[0]^=nums.pop()
            i-=1
        return nums[0]



# Faster than 97.90%
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums.pop()
        idx = len(nums) >> 1
        while idx:
            ans ^= nums[idx-1] ^ nums[-idx]
            idx-=1
        return ans
