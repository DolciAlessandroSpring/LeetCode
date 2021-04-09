import unittest
import random
import sys

random.seed(10)

# from two_sum import Solution

from typing import List
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
         
        return solution


class TestTwoSum(unittest.TestCase):

    def test_random(self):
        nums = random.sample(range(-20, 20), 20)
        target = random.randint(-40, 40)
        result = Solution().twoSum(nums, target, False)
        self.assertEqual(result, [0, 8])
    
    def test_random2(self):
        nums = random.sample(range(-20, 20), 10)
        target = random.randint(-10, 10)
        result = Solution().twoSum(nums, target, False)
        self.assertEqual(result, [5, 9])

    def test_no_solution(self):
        nums = [1, 2, 3, 4, 5, 6]
        target = 12
        result = Solution().twoSum(nums, target, False)
        self.assertIsNone(result)

    def test_equal_number(self):
        nums = [3, 3]
        target = 6
        result = Solution().twoSum(nums, target, False)
        self.assertEqual(result, [0, 1])


if __name__ == '__main__':
    unittest.main()
