'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = None
        lookup = dict()
        '''
        first iteration is to build the lookup
        '''
        for i, num1 in enumerate(nums):
            lookup[num1] = i
        '''
        second iteration is to find the complement from the lookup
        '''
        for i, num1 in enumerate(nums):
            complement = target - num1
            if complement in lookup.keys() and lookup[complement] != i:
                result = [i, lookup[complement]]
                break
            
        return result

testcases = list()
#add haystack and needle
testcases.append([[2,7,11,15], 9])
testcases.append([[3,2,4], 6])
testcases.append([[3,3], 6])
testcases.append([[], 6])
testcases.append([[6,6], 6])
testcases.append([[1,2,7,11,15], 6])
testcases.append([[-2,-1,1,2,7,11,15], 6])
testcases.append([[-2,-1,1,2,7,8,11,15], 6]) # constraint violation; multiple solution
solution = Solution()
for i, testcase in enumerate(testcases):
    nums = testcase[0]
    target = testcase[1]
    result = Solution.twoSum(solution, nums, target)
    print(f'{i+1} - given array {nums} and target {target}. The result is {result}')