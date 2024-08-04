class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle division by zero
        if divisor == 0:
            return INT_MAX
        
        # Handle overflow cases
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the quotient
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Take the absolute value of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                i <<= 1
            dividend -= temp
            quotient += i
        
        # Apply the sign to the quotient
        quotient = sign * quotient
        
        # Handle overflow
        if quotient < INT_MIN:
            return INT_MIN
        elif quotient > INT_MAX:
            return INT_MAX
        else:
            return quotient
