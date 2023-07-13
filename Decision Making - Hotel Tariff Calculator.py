Decision Making - Hotel Tariff Calculator
Jon Snow and the men in the north decided to open Castle Black for the northerners and the Castle was turned into a Hotel. The Hotel was flourishing
and there was high demand for the rooms. So Jon Snow decided to modify the tariff accordingly. Write a program to calculate the hotel tariff. The room rent
  is 20% high during peak seasons [April-June and November-December].

Input Format

The first input integer denotes the count of the month. The second input integer denotes the room rent per day. The third input integer denotes 
the number of days stayed in the hotel.

Output Format
Print the hotel tariff to be paid. (Note: if the month value entered is not ranging from 1-12, print as Invalid Input)

Sample Input 0
3
1500
2

Sample Output 0
3000

Sample Input 1
14
1500
2

Sample Output 1
Invalid Input

Python Code:

month= int(input())
room_rent=int(input())
num_days=int(input())
peak_months = [4, 5, 6, 11, 12]
if month < 1 or month > 12:
    print("Invalid Input")
else:
    room_rent_total = room_rent * num_days
    if month in peak_months:
        room_rent_total *= 1.2
    print(int(room_rent_total))
