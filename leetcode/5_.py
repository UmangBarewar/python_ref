class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(num):
            # Convert number to string to easily check palindrome property
            num_str = str(num)
            
            # Check if the number reads the same forwards and backwards
            return num_str == num_str[::-1]
        
        if is_palindrome(s):
            return s
        
        # Placeholder for the longest palindrome found
        longest_palindrome = ""
        
        # Iterate through all possible substrings
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
        
        return longest_palindrome
