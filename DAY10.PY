#MISSING NUMBER
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        largest_value = len(nums)
        missing = 0
        for i in range(len(nums)):
            
            missing += (largest_value - i) - nums[i]
        return missing

if __name__ == "__main__":
    solution = Solution()
    
    input_1 = [3, 0, 1]
    output_1 = solution.missingNumber(input_1)
    print(f"Input: {input_1} -> Missing Number: {output_1}") 
    input_2 = [0, 1]
    output_2 = solution.missingNumber(input_2)
    print(f"Input: {input_2} -> Missing Number: {output_2}")  
    input_3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    output_3 = solution.missingNumber(input_3)
    print(f"Input: {input_3} -> Missing Number: {output_3}")  



#MAJORITY ELEMENT
class Solution(object):
    def majorityElement(self, nums):
        
        count = 0
        majority = 0
        for i in range(len(nums)):
            if count == 0 and majority != nums[i]:
                
                majority = nums[i]
                count = 1
            elif majority == nums[i]:
                
                count += 1
            else:
                
                count -= 1
                
        return majority


if __name__ == "__main__":
    
    solution = Solution()
    input_1 = [3, 2, 3]
    output_1 = solution.majorityElement(input_1)
    print(f"Input: {input_1} -> Majority Element: {output_1}")
    input_2 = [2, 2, 1, 1, 1, 2, 2]
    output_2 = solution.majorityElement(input_2)
    print(f"Input: {input_2} -> Majority Element: {output_2}")


#MERGE INTERVALS

class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end


    def __repr__(self):
        return f"[{self.start}, {self.end}]"

class Solution:
    def merge(self, intervals):
        out = []

        for i in sorted(intervals, key=lambda i: i.start):
            
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:

                out.append(i) 
        return out


if __name__ == "__main__":

    input_data = [
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18)
    ]
    
    print("Original Intervals:", input_data)
    sol = Solution()
    merged_intervals = sol.merge(input_data)
    
    print("Merged Intervals:  ", merged_intervals)
