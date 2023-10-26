Decision Making - Gift for Birthday
Penny is celebrating her 25th birthday. Her friend Leonard promised her that he will buy her a pair of new shoes on her birthday if she 
solves the question asked by him. He asks Penny to find out whether the year in which she was born is a leap year or not. Help her to solve this
puzzle so that she celebrates her birthday happily. If her birth year is 1995 and it is a leap year display “1995 is a leap year.” Else display 
“1995 is not a leap year.”

Input Format
The input consists of 1 integer.

Output Format
The output consists of 1 string.

Sample Input 0
2016

Sample Output 0
2016 is a leap year

Sample Input 1
1999

Sample Output 1
1999 is not a leap year

Python Code
def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year=int(input())
if leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
