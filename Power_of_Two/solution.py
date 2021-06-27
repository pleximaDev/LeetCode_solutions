# https://leetcode.com/problems/power-of-two/
# one-liner
# faster than 86.58%, 28 ms
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bool(n) if n in (0,1) else False if n<0 else not bool(n&(n-1))
