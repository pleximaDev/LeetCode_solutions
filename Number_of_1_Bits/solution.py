# https://leetcode.com/problems/number-of-1-bits/
# Hamming Wheight
# Faster than 95.62%, 24 ms
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter=0
        while n>0:
            counter+=n&1
            n>>=1
        return counter
