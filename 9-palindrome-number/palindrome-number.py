class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0 :
            return False

        reversed_number= 0
        original_number = x

        temp_x = x

        while temp_x > 0:

            last_digit = temp_x % 10
            reversed_number = (reversed_number * 10) + last_digit
            temp_x = temp_x / 10
        
        return original_number == reversed_number