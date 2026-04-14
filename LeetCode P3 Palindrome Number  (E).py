class Solution(object):
    def isPalindrome(self, x):
        res = str(x)
        return res == res[::-1]
    
if __name__ == "__main__":
    sol = Solution()
    
    test_val = 121
    result = sol.isPalindrome(test_val)
    
    print(f"Is {test_val} a palindrome? {result}")