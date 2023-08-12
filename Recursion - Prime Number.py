Recursion - Prime Number
Write a program to find whether the given number is a prime number or not using recursion.

Input Format
The Input consists of an integer.

Output Format
Prints Prime Number or Not a Prime number.

Sample Input 0
13
  
Sample Output 0
Prime Number
  
Sample Input 1
246
  
Sample Output 1
Not a Prime Number

Python Code:

def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)
def main():
    number = int(input())
    if is_prime(number):
        print("Prime Number")
    else:
        print("Not a Prime Number")
if __name__ == "__main__":
    main()
