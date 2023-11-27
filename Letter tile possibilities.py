Letter tile possibilities
You have n tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Input Format
String S

Constraints
1 <= tiles.length <= 7
tiles consists of uppercase English letters.

Output Format
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Sample Input 0
ABB

Sample Output 0
8

Explanation 0
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Sample Input 1
AAABBC

Sample Output 1
188

Python Code:

def count_sequences(tiles):
    def backtrack(index, current_sequence):
        nonlocal result
        result.add(current_sequence)
        for i in range(len(tiles)):
            if not used[i]:
                used[i] = True
                backtrack(i, current_sequence + tiles[i])
                used[i] = False
    result = set()
    used = [False] * len(tiles)
    for i in range(len(tiles)):
        used[i] = True
        backtrack(i, tiles[i])
        used[i] = False
    return len(result)
tiles_0 = input()
print(count_sequences(tiles_0))
