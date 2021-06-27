# https://leetcode.com/problems/plus-one/
# faster than 99.70%, 20 ms

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            digits[i] = (digits[i]!=9)*(digits[i] + 1)
            if digits[i]:
                return digits
            elif i == 0:
                digits.insert(0,1)
                return digits
            else:
                i-=1
