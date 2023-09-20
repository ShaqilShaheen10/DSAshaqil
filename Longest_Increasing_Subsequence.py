You are given an array arr of size N, your task is to re-order the array and find the length of the longest increasing sub-sequence from that re-ordered array and print the same as the output

A sub-sequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements

Input Format:

The input is in the following format:

The first line contains N, denoting the number of elements in the array arr. . Then, N subsequent lines contain a single integer, denoting the value of the ith element of the array arr.

The input will be read from the STDIN by the candidate

Output Format:

Print the length of the longest increasing sub-sequence after re-ordering the given array.

The output will be matched to the candidate's output printed on the STDOUT

Constraints:

1≤ N ≤ 105.

• 15 arr[i]≤ 105. .

Example:

Input:

5

5

3

3

3

1

Output:

3

Explanation:

Let's re-order the elements, as (1,3,5,3,3). Now, we can find the longest increasing sub-sequence of this array, which will be (1,3,5), and its length is 3. There can be several other re-orderings of the array, but the longest increasing sub-sequence size that we can obtain for this particular array is 3, which is thus, the answe to the problem
