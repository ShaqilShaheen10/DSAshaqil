
XOR Approach for Duplicates

There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.

This is one of those problems.

Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

Food for thought :

Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
Obviously approach 1 is more susceptible to overflows.
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

Python Code:

def find_duplicate_and_missing(nums):
    n = len(nums)
    xor_all = 0

    # First, XOR all the elements from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all the elements in the input array
    for num in nums:
        xor_all ^= num

    # Find the rightmost set bit in xor_all
    rightmost_set_bit = xor_all & -xor_all

    # Initialize two variables to track the missing and duplicate elements
    missing = 0
    duplicate = 0

    # XOR the elements in the input array based on the rightmost set bit
    for num in nums:
        if num & rightmost_set_bit:
            missing ^= num
        else:
            duplicate ^= num

    # XOR the numbers from 1 to n based on the rightmost set bit
    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            missing ^= i
        else:
            duplicate ^= i

    # Check which number is missing from the input array
    for num in nums:
        if num == missing:
            return [missing, duplicate]

    return [duplicate, missing]

# Test the function with the given example
input_array = [3, 1, 2, 5, 3]
output = find_duplicate_and_missing(input_array)
print(output)  # Output: [3, 4]  (A = 3, B = 4)
