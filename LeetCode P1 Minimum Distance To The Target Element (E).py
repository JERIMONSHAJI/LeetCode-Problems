class Solution(object):
    def getMinDistance(self, nums, target, start):
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(res, abs(i - start))
        return res

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 1]
    target = 1
    start = 3
    
    sol = Solution()
    res = sol.getMinDistance(nums, target, start)
    
    print(res)