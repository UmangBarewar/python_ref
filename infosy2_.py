def vacation(d, o, k, obj):
    L = 0
    max_days = 0
    
    # Sort the obligations to apply the sliding window technique
    obj.sort()
    
    for R in range(o):
        # Check if the current window exceeds the allowed cancellation limit
        while obj[R] - obj[L] + 1 - (R - L + 1)> k:
            L += 1
        
        # Calculate the vacation length for the current window
        vacation_len = obj[R] - obj[L] 
        max_days = max(max_days, vacation_len)
    
    # Handle edge cases
    # If there are no obligations
    if o == 0:
        return d
    
    # If the number of cancellations allowed is greater than or equal to the number of obligations
    if k >= o:
        return d
    
    return max_days

# Input
D = int(input("Enter the total number of days: "))
O = int(input("Enter the number of obligations: "))
K = int(input("Enter the number of obligations he can cancel: "))
obg_days = list(map(int, input("Enter the obligation days separated by spaces: ").split()))

# Function call
x = vacation(D, O, K, obg_days)
print(x)
