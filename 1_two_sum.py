
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from typing import List
import random

class Solution:
    def twoSum(self, nums: List[int], target: int, debug: bool) -> List[int]:

        solution = None
        
        # take the first of the two numbers (leave space for the second number)
        for i in range(len(nums)-1):
            
            # search for the second number
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    solution = [i, j]
                    break
            
            # break as soon as you find the solution
            if solution is not None:
                break
         
        if solution is None:
            print("Solution not found")
        else:
            return solution

# create class
s = Solution()

# create input
nums = random.sample(range(-20, 20), 20)
print("Numbers: ", nums)

target = random.randint(-40, 40)
print("Target: ", target)

sol = s.twoSum(nums, target, debug = True)
print("The solution is: ", sol, "  --   which uses the sum of", nums[sol[0]], "and", nums[sol[1]])
