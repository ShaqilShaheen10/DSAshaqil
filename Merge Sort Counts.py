Merge Sort Counts(Hackerrank)

Merge sort is one of the most well-known sorting algorithms. In this problem, mergesort takes an array of unique integers as a parameter and returns 
the sorted array.

An array has n elements. If the array has less than 2 elements, then the array is returned without any changes. If the array has more than two elements,
then it is divided into two arrays, left and right. The left array contains the first half elements of the input array while the right array contains the
second half of the elements. If nis odd, the left array takes the middle element. Next, the algorithm calls itself first with the left array and then with 
the right array.

After that, the algorithm produces the sorted array, by merging the left and the right arrays into a single sorted array. In this challenge,
keep a count for each of the elements in the input array. Initially, all counts are 0. Whenever an integer k from the right array is merged before at
least one element from the left array, add 1 to the count. Find the maximum count value after the merge sort algorithm finishes.

Input
STDIN     Function
3      - >  arr[] size n=3
2      - >arr=[2, 1, 3]
1
3

Output
1

Python Code:

def largestCountValue(a):
    # Function to merge two sorted arrays and calculate the count
    def merge(left, right):
        i = j = count = 0
        merged = []

        while i < len(left) and j < len(right):
            if right[j] < left[i]:
                merged.append(right[j])
                count += len(left) - i
                j += 1
            else:
                merged.append(left[i])
                i += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, count

    # Function to perform merge sort and return the maximum count
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = merge_sort_count(arr[:mid])
        right, right_count = merge_sort_count(arr[mid:])
        merged, merge_count = merge(left, right)

        return merged, left_count + right_count + merge_count

    _, max_count = merge_sort_count(a)
    return max_count

# Example usage:
a = [2, 1, 3]
result = largestCountValue(a)
print(result)  # Output: 1
