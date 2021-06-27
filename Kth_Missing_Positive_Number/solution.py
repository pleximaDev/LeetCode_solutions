# https://leetcode.com/problems/kth-missing-positive-number/
# faster than 94.88%, 44 ms
# memory used less than 96.96%
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = 1
        counter = 1 if arr[0] != 1 else 0 #faster than int() and 1*(!=)
        i = 1 - counter
        while counter != k:
            res += 1
            if i < len(arr) and res == arr[i]:
                i += 1
            else:
                counter += 1
        del counter, i
        return res
