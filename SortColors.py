Sort Colors(LeeTCode)
To solve this problem, we can use the "Dutch National Flag" algorithm, which is a one-pass algorithm that sorts an array containing three distinct elements. 
In this case, the three distinct elements are 0, 1, and 2, representing the colors red, white, and blue.

Here's the step-by-step approach to implement the algorithm:

1.Initialize three pointers: left, current, and right. Set left and current to the start of the array (index 0) 
and right to the end of the array (index n-1), where n is the length of the array.
2.Iterate while current is less than or equal to right.
3.If nums[current] is 0, swap nums[current] with nums[left], increment both current and left by 1.
4.If nums[current] is 1, increment current by 1 and continue to the next iteration.
5.If nums[current] is 2, swap nums[current] with nums[right], decrement right by 1.
6.Repeat steps 2-5 until current is greater than right.
7.At this point, the array will be sorted in the required order.

  
Python code:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low,mid,high=0,0,len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
        return nums
