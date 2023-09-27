Arrays 1D - Sum of even numbers and odd numbers
Mahe and Mani are playing a puzzle game with a given set of numbers. They need to find the sum of the odd number and the even number. 
Write a program to help them to solve the puzzle game.

Input Format

Input consists of n+1 integers. The first integer corresponds to ‘n’, the size of the array. The next ‘n’ integers correspond to the elements 
in the array. Assume that the maximum value of n is 15.

Output Format
Refer to the sample output for details.

Sample Input 0
5
2
3
6
8
-1

Sample Output 0
The sum of the even numbers in the array is 16
The sum of the odd numbers in the array is 2

Sample Input 1
4
1
2
3
-1

Sample Output 1
The sum of the even numbers in the array is 2
The sum of the odd numbers in the array is 3

Python Code:

def sum_odd_and_even(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum
def main():
    n = int(input())
    array = []
    for _ in range(n):
        num = int(input())
        array.append(num)
    even_sum, odd_sum = sum_odd_and_even(array)
    print("The sum of the even numbers in the array is", even_sum)
    print("The sum of the odd numbers in the array is", odd_sum)
if __name__ == "__main__":
    main()
