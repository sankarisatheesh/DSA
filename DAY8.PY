#1 
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        for _ in range(2, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
            
        return prev1


sol = Solution()
test_input = 6
print(f"The {test_input}th Fibonacci number is: {sol.fib(test_input)}")


#2
class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        
        dp = [-1] * (n + 1)
        return self.climbStairsHelper(n, dp)

    def climbStairsHelper(self, n, dp):
        if n <= 1:
            return 1
        
        if dp[n] != -1: 
            return dp[n]
    
        dp[n] = self.climbStairsHelper(n - 1, dp) + self.climbStairsHelper(n - 2, dp)
        return dp[n]

sol = Solution()
input_stairs = 5
output_ways = sol.climbStairs(input_stairs)

print(f"Input: n = {input_stairs}")
print(f"Output: {output_ways}")


#3
class Solution(object):
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current, open_count, close_count):
            
            if len(current) == 2 * n:
                result.append(current)
                return
            

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
                
            
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
                
        
        backtrack("", 0, 0)
        return result


sol = Solution()
input_1 = 2
output_1 = sol.generateParenthesis(input_1)
print(f"Input: n = {input_1}")
print(f"Output: {output_1}\n")


input_2 = 3
output_2 = sol.generateParenthesis(input_2)
print(f"Input: n = {input_2}")
print(f"Output: {output_2}\n")


input_3 = 4
output_3 = sol.generateParenthesis(input_3)
print(f"Input: n = {input_3}")
print(f"Total combinations found: {len(output_3)}")
print(f"Output: {output_3}")