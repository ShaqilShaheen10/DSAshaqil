Excel Column Number
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Input Format
A column number is given to you.

Output Format
Give the title of that column number.

Sample Input 0
A

Sample Output 0
1

Sample Input 1
AB

Sample Output 1
28

Python Code:

def titleToNumber(columnTitle):
    columnNumber = 0
    for char in columnTitle:
        char_value = ord(char) - ord('A') + 1
        columnNumber = columnNumber * 26 + char_value
    return columnNumber
columnTitle1 = input()
columnNumber1 = titleToNumber(columnTitle1)
print(columnNumber1)
