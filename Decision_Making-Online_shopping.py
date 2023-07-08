Decision Making - Online shopping
Richard Castle wants to buy a shirt. As he is very lazy, he decided to buy the shirt online. He chooses a shirt on Flipkart and is surprised to see the same 
shirt on Snapdeal, and Amazon as well. So he decided to buy the shirt from the website which offers the least price. The price of the shirt, the discount percentage,
and the shipping charges of all three websites have been given as input. Help him in calculating the price of the shirt on each website and decide which website 
has the lowest price.If the price in all the three websites are same then first priority goes to Flipkart, then Snapdeal and finally Amazon.

Input Format

Input consists of 9 integers. The first three input corresponds to Flipkart details such as the price of the shirt, discount offered, and shipping charges. 
The next three input corresponds to Snapdeal details such as the price of the shirt, discount offered, and shipping charge. The last three input corresponds
to Amazon details such as the price of the shirt, discount offered, and shipping charge.

Output Format

The Output consists of three integers that denote the prices on Flipkart, Snapdeal, and Amazon and should suggest the website that has the lowest price.

Sample Input 0
1000
50
50
900
50
70
800
10
200

Sample Output 0
In Flipkart: Rs.550
In Snapdeal: Rs.520
In Amazon: Rs.920
Choose Snapdeal

Sample Input 1
1000
60
80
900
50
30
1000
10
200

Sample Output 1
In Flipkart: Rs.480
In Snapdeal: Rs.480
In Amazon: Rs.1100
Choose Flipkart

Python Code:
def Flipkart(a,b,c):
    dis=(b/100)*a
    Ftot=(a-dis)+c
    return int(Ftot)
def Snapdeal(e,f,g):
    dis=(f/100)*e
    Stot=(e-dis)+g
    return int(Stot)
def Amazon(h,i,j):
    dis=(i/100)*h
    Atot=(h-dis)+j
    return int(Atot)
a=int(input())
b=int(input())
c=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())
i=int(input())
j=int(input())
F=Flipkart(a,b,c)
S=Snapdeal(e,f,g)
A=Amazon(h,i,j)
print(f"In Flipkart: Rs.{F}")
print(f"In Snapdeal: Rs.{S}")
print(f"In Amazon: Rs.{A}")
if (F<=S)&(F<A):
    print("Choose Flipkart")
elif (S<F)&(S<A):
    print("Choose Snapdeal")
else:
    print("Choose Amazon")
    
