Remove All Adjacent Duplicates in String II
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and 
the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Input Format
First Line String S
Second line Integer K

Constraints
1 <= s.length <= 105
2 <= k <= 104
s only contains lowercase English letters.

Output Format
Return the final string after all such duplicate removals have been made.

Sample Input 0
abcd
2

Sample Output 0
abcd

Explanation 0
Explanation: There's nothing to delete.

Sample Input 1
deeedbbcccbdaa
3

Sample Output 1
aa

Explanation 1
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Python Code:

def removeDuplicates(s, k):
    stack = []
    for char in s:
        if not stack or stack[-1][0] != char:
            stack.append([char, 1])
        else:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
    result = ""
    for char, count in stack:
        result += char * count
    return result
s = input()
k = int(input())
result = removeDuplicates(s, k)
print(result)
