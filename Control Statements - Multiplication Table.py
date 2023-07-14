Control Statements - Multiplication Table
Penny wanted to complete her graduation from the Community College of California. But being the newbee she is , she does not how to multiply two numbers. 
Sheldon being a good friend wanted to help Penny by writing a program to print the multiplication table of an integer n.

Input Format
Input consists of 2 integers. The first integer corresponds to n. The second integer corresponds to m(rows).

Output Format
Refer to the sample output for formatting specifications.

Sample Input 0
5
4

Sample Output 0
Enter n
Enter m
The multiplication table of 5 is
1*5=5
2*5=10
3*5=15
4*5=20

Explanation 0
Multiplication of the 5th table from 1 to 4 is printed.

Sample Input 1
5
6

Sample Output 1
Enter n
Enter m
The multiplication table of 5 is
1*5=5
2*5=10
3*5=15
4*5=20
5*5=25
6*5=30

Explanation 1
Multiplication of the 5th table from 1 to 6 is printed.

Python Code:

n=int(input("Enter n\n"))
m=int(input("Enter m\n"))
print(f"The multiplication table of",n,"is")
for i in range(1,m+1):
    print(i,"*",n,"=",i*n,sep="")
    
