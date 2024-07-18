class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Trim leading and trailing whitespace
        s = s.strip()
        
        if not s:
            return 0
        
        # Step 2: Determine sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]  # Move past the '-'
        elif s[0] == '+':
            s = s[1:]  # Move past the '+'
        
        # Step 3: Convert numerical characters
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break
        
        # Step 4: Apply sign and handle overflow
        result = sign * result
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
