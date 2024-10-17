#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    operations, factor = 0, 2
    while factor <= n:
        # if n evenly divides by factor
        if n % factor == 0:
            # total even-divisions by factor = total operations
            operations += factor
            # set n to the remainder
            n = n / factor
            # reduce factor to find remaining smaller vals that evenly-divide n
            factor -= 1
        # increment factor until it evenly-divides n
        factor += 1
    return operations
