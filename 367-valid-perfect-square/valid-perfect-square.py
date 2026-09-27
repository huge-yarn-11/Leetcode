class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        ans = False
        while low <= high:
            mid = low + (high - low) // 2
            if mid* mid == num:
                ans = True
                break
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return ans