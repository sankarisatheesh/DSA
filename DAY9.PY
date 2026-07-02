#1 
class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
        return False
sol = Solution()

input_1 = [1, 2, 3, 1]
result_1 = sol.containsDuplicate(input_1)
print(f"Input: {input_1} -> Output: {result_1}") 
input_2 = [1, 2, 3, 4]
result_2 = sol.containsDuplicate(input_2)
print(f"Input: {input_2} -> Output: {result_2}") 


#2 
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i]) - ord("a")] += 1
            arr[ord(t[i]) - ord("a")] -= 1

        for check in arr:
            if check != 0:
                return False

        return True
if __name__ == "__main__":
    solution = Solution()

    
    string1 = "anagram"
    string2 = "nagaram"
    result1 = solution.isAnagram(string1, string2)
    print(f"Are '{string1}' and '{string2}' anagrams? {result1}")

    string3 = "rat"
    string4 = "car"
    result2 = solution.isAnagram(string3, string4)
    print(f"Are '{string3}' and '{string4}' anagrams? {result2}")
    
    
#3
from typing import List

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] = frequency[num] + 1
        
        frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        
    
        result = list(frequency.keys())[:k]
        return result

if __name__ == "__main__":
    solution = Solution()
    
    input_nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    output1 = solution.topKFrequent(input_nums1, k1)
    print(f"Input: nums = {input_nums1}, k = {k1}")
    print(f"Output: {output1}\n")
    
    input_nums2 = [4, 4, 4, 4, 2, 2, 9]
    k2 = 1
    output2 = solution.topKFrequent(input_nums2, k2)
    print(f"Input: nums = {input_nums2}, k = {k2}")
    print(f"Output: {output2}\n")
    
    
    input_nums3 = [1]
    k3 = 1
    output3 = solution.topKFrequent(input_nums3, k3)
    print(f"Input: nums = {input_nums3}, k = {k3}")
    print(f"Output: {output3}")


