Candy 13
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
  
Input Format
First line array size
Second line array elements

Constraints
n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104

Output Format
Return the minimum number of candies you need to have to distribute the candies to the children.

Sample Input 0
3
1 0 2

Sample Output 0
5

Sample Input 1
3
1 2 2

Sample Output 1
4

Pyhton Code:

def min_candies(ratings):
    n = len(ratings)
    left_to_right = [1] * n
    right_to_left = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left_to_right[i] = left_to_right[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right_to_left[i] = right_to_left[i + 1] + 1
    total_candies = 0
    for i in range(n):
        total_candies += max(left_to_right[i], right_to_left[i])
    return total_candies
n = int(input())
ratings = list(map(int, input().split()))
result = min_candies(ratings)
print(result)
