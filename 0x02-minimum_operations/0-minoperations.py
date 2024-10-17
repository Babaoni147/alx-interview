#!/usr/bin/python3
'''Minimum Operations python3 challenge'''



def minOperations(n):
    '''Calculates the fewest number of operations needed to result in exactly n H characters.'''
    
    # If n is less than or equal to 1, we return 0 because it's impossible
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2  # Start with the smallest factor
    
    # Keep dividing n by its factors, starting with 2 and going up
    while n > 1:
        # While n is divisible by the current factor
        while n % factor == 0:
            # Add the factor to the operations count (because you copy and paste that many times)
            operations += factor
            # Divide n by this factor
            n //= factor
        # Move to the next factor
        factor += 1
    
    return operations
