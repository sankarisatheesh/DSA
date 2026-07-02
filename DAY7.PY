# 1
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_scores = [0] * (n + 1)
        
        for truer, trustee in trust:
            trust_scores[truer] -= 1
            trust_scores[trustee] += 1
            
        for person in range(1, n + 1):
            if trust_scores[person] == n - 1:
                return person
                
        return -1
sol = Solution()
print("Output 1:", sol.findJudge(n=2, trust=[[1, 2]])) 
print("Output 2:", sol.findJudge(n=3, trust=[[1, 3], [2, 3]])) 
print("Output 3:", sol.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]])) 


#2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        freq = [0] * 26
        for c in magazine:
            freq[ord(c) - ord('a')] += 1
            
        for c in ransomNote:
            idx = ord(c) - ord('a')
            if freq[idx] == 0:
                return False
            freq[idx] -= 1
            
        return True


if __name__ == "__main__":
    solution = Solution()
    note1, mag1 = "a", "b"
    print(f"Ransom Note: '{note1}', Magazine: '{mag1}' -> Can Construct: {solution.canConstruct(note1, mag1)}")
    note2, mag2 = "aa", "ab"
    print(f"Ransom Note: '{note2}', Magazine: '{mag2}' -> Can Construct: {solution.canConstruct(note2, mag2)}")
    note3, mag3 = "aa", "aab"
    print(f"Ransom Note: '{note3}', Magazine: '{mag3}' -> Can Construct: {solution.canConstruct(note3, mag3)}")
    

#3
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: 
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid: list[list[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        
        grid[i][j] = '#' 
        
        self.dfs(grid, i + 1, j) 
        self.dfs(grid, i - 1, j) 
        self.dfs(grid, i, j + 1) 
        self.dfs(grid, i, j - 1) 
if __name__ == "__main__":
    solver = Solution()

    
    input_grid_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    input_grid_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(f"Result for Grid 1: {solver.numIslands(input_grid_1)}") 
    print(f"Result for Grid 2: {solver.numIslands(input_grid_2)}") 
