# https://leetcode.com/problems/rotate-array/

class Solution: # faster than 95%, 196 ms
    def rotate(self, nums: List[int], k: int) -> None:
        if k%len(nums):
            nums.extend(nums[:-k%len(nums)]+[k%len(nums)])
            del nums[:-(1+int((len(nums)-nums[-1])/2)+nums[-1])]
            nums.pop()




"""
class Solution: # faster than 93.79%, 200 ms
    def rotate(self, nums: List[int], k: int) -> None:
        if k%len(nums):
            k %= len(nums)
            nums.extend(nums[:-k])
            del nums[:-(int((len(nums) - k)/2) + k)]
"""
