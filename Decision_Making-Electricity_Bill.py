Decision Making - Electricity Bill
In the city of Rajkot, Gujarat the Golden company is taking care of the expenses for the Court's discussion room.
Due to continuous discussions regarding the upcoming 'Ring Road' project at Rajkot, the electricity bill was high and they need to pay it with all the money they have.
The electricity board has decided to charge money based on the units consumed by a particular home. If the units consumed are less than or equal to 200,
the cost for one unit is 0.5paise. If the unit is less than or equal to 400, the cost for one unit is 0.65paise plus Rs.100 extra charge.
If the unit is less than or equal to 600, the cost for one unit is 0.80paise plus Rs.200 extra charge. 
If the unit is greater than 600 the cost for one unit is Rs.1.25 plus Rs.425 extra charge. You need to calculate the electricity bill based on the units consumed.

Input Format

Input consists of one integer which corresponds to the units consumed.

Output Format

The output consists of one integer which corresponds to the electricity bill in Rupees.

Sample Input 0

200
Sample Output 0

Rs.100
Explanation 0

Here, the units consumed are equal to 200, and the cost for one unit is 0.5. Hence the electricity bill will be Rs.100.

Python Code:
units_consumed = int(input())
if units_consumed <= 200:
    cost_per_unit = 0.5
    extra_charge = 0
elif units_consumed <= 400:
    cost_per_unit = 0.65
    extra_charge = 100
elif units_consumed <= 600:
    cost_per_unit = 0.8
    extra_charge = 200
else:
    cost_per_unit = 1.25
    extra_charge = 425
electricity_bill = int(units_consumed * cost_per_unit + extra_charge)
print(f"Rs.{electricity_bill}")
