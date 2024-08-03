# Given a number M in its decimal representation, your task is find the minimum base B such that in the 
# representation of M at base B all digits are the same


def find_minimum_base(M):
    # Start with base B = 2
    for B in range(2, M + 1):
        # Let's represent the number M in base B
        # Initialize an empty list to store digits
        num_in_base_B = []
        number = M
        
        while number > 0:
            num_in_base_B.append(number % B)
            number //= B
        
        # Check if all digits are the same
        if all(d == num_in_base_B[0] for d in num_in_base_B):
            return B
    
    # If no base is found, return -1 (this case shouldn't normally happen)
    return -1

# Example usage:
M = int(input("Enter the number"))
print(find_minimum_base(M))
