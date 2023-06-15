*/ Next Permutation
 A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

Algorithm:
1.Start from the rightmost element of the given sequence and search for the first pair of adjacent elements where the 
left element is smaller than the right element. Let's call the index of the left element "i". If no such pair exists,
it means the given sequence is the last permutation. In that case, reverse the entire sequence to get the first permutation and return.

2.Once you find the pair from step 1, search for the smallest element in the subsequence to the right of "i" that
is greater than the element at index "i". Let's call the index of this element "j".

3.Swap the elements at indices "i" and "j".

4.Reverse the subsequence to the right of index "i" (including index "i" itself).

Python Code /*

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N=len(nums)
        if N<=2:
            return nums.reverse()
        P=N-2
        while P>=0 and nums[P]>=nums[P+1]:
            P-=1
        if P==-1:
            return nums.reverse()
        for x in range(N-1,P,-1):
            if nums[P]<nums[x]:
                nums[P],nums[x]=nums[x],nums[P]
                break
        nums[P+1:]=reversed(nums[P+1:])
