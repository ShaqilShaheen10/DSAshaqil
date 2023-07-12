Decision Making - Number of Days
The given are two positive integers Year and Month, the task is to find the number of days corresponding to each month of the given year where 1 is January,
2 is February, 3 is March, and so on.

Note: The Input range of year: Minimum Year = 1900 and Maximum Year = 9999 i.e (1900<=Year<=9999). The Input range of month: Minimum Month = 12 
and Maximum Year = 12 i.e (1<=month<=12) If the given year does not lie between the given range, output 0.

Input Format
The input consists of two lines. The first line contains an integer, which is the Year. The second line contains an integer, which is the Month.

Output Format
The output prints the number of days. Refer to the sample output

Sample Input 0
2000
2

Sample Output 0
29 Days

Explanation 0
In a given year 7 months consist of 31 days 4 months consist of 30 days 2nd month consists of 28 days (29 days if leap year) Given year=2000 
and month=2 (i.e) February 2000 consists of 29 days

Sample Input 1
1999
8

Sample Output 1
31 Days

Explanation 1
In a given year 7 months consist of 31 days 4 months consist of 30 days 2nd month consists of 28 days (29 days if leap year) Given year=1999 
and month=8 (i.e) August 1999 consists of 31 days


Python Code

def number_of_days_in_month(year, month):
    if month == 2:
        return 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30
if __name__ == "__main__":
    year = int(input())
    month = int(input())
    number_of_days = number_of_days_in_month(year, month)
    print(f"{number_of_days} Days")
