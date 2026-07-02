#Valid paranthesis

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack


sol = Solution()
print(sol.isValid("()[]{}")) 
print(sol.isValid("(]"))      


#Implement Queue using stacks

class MyQueue(object): 
    def __init__(self): 
        self.in_stk = [] 
        self.out_stk = [] 

    def push(self, x): 
        self.in_stk.append(x) 

    def pop(self): 
        self.peek() 
        return self.out_stk.pop() 

    def peek(self): 
        if not self.out_stk: 
            while self.in_stk: 
                self.out_stk.append(self.in_stk.pop()) 
        return self.out_stk[-1] 

    def empty(self): 
        return not self.in_stk and not self.out_stk

queue = MyQueue()
queue.push(1)
print(queue.peek())  


#daily temperatures

class Solution: 
    def dailyTemperatures(self, temperatures): 
        stack = [] 
        ans = [0] * len(temperatures) 
        for i in range(len(temperatures)): 
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                prev = stack.pop() 
                ans[prev] = i - prev 
            stack.append(i) 
        return ans

sol = Solution()
test_input = [73, 74, 75, 71, 69, 72, 76, 73]
output = sol.dailyTemperatures(test_input)
print("Output:", output)

