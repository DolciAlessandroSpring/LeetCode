
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

class Solution:
    def reverse(self, x: int, debug: bool) -> int:
        
        print("The input number is: ", x)
        
        sign_x = 1 if x>= 0 else -1
        if debug:
            print("It's sign function is: ", sign_x)
        
        x_inv = int(str(abs(x))[::-1]) * sign_x
        if debug:
            print("Inverted number: ", x_inv)
        
        # constrains
        cond_1 = x_inv < -2**31
        cond_2 = x_inv > 2**31 - 1
        if debug:
            print("The constrains are ", (-2**31 - 1), " and ", 2**31)
            print("Status of the conditions: ", cond_1, " and ", cond_2)
        
        if (cond_1 | cond_2):
            x_inv = 0
        
        print("The solution is: ", x_inv)
        return(x_inv)

# create class
s = Solution()

# create input
test = [0, 3, 567, -460, 8735468047]
print("Numbers: ", test)

[s.reverse(x, debug = False) for x in test]

