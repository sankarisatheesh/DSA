#TWO SUM 

def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return complement 
arr = [2, 7, 11, 15]
target = 9

print(two_sum(arr, target))

#PALINDROME

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
            
        return x == reversed_half or x == reversed_half // 10
solver = Solution()
user_num = int(input("Enter an integer to check: "))
result = solver.isPalindrome(user_num)
print(f"Is it a palindrome? {result}")

#LONGEST SUBSTRING LENGTH
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    res = max(res, j - i + 1)
        return res


if __name__ == "__main__":
   
    sol = Solution()
    
   
    test_input = "abcabcbb"
    
    
    output = sol.lengthOfLongestSubstring(test_input)
    
   
    print("--- OUTPUT ---")
    print(f"Input String: '{test_input}'")
    print(f"Result Length: {output}")
    print("--------------")


	   

	 

	 






