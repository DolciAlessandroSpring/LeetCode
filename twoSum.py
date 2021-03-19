
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        solution = None
        
        # take the first of the two numbers (leave space for the second number)
        for i in range(len(nums)-1):
            #print("i is", i)
            
            # search for the second number
            for j in range(i+1, len(nums)):
                #print("j is", j)
                
                if nums[i] + nums[j] == target:
                    #print("Solution found:", nums[i], " and ", nums[j])
                    solution = [i, j]
                    break
            
            # break as soon as you find the solution
            if solution is not None:
                break
         
        if solution is None:
            print("Solution not found")
        else:
            return solution
