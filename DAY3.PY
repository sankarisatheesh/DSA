#Searching &Sorting Algorithms
#Binary Search (704)
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
obj = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(obj.search(nums, target))

#Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
obj = Solution()
nums = [1, 3, 5, 6]
target = 5
print(obj.searchInsert(nums, target))

#search in rotated sorted array 
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
obj = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(obj.search(nums, target))