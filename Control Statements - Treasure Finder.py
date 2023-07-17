Control Statements - Treasure Finder
Nikitha and Danny are close friends. They both are studying in the same school. Now they are on summer vacation. As they are bored, they ask their parents
to take them to an exhibition. Nikitha and Danny play a game. In this game, there are three boxes with some number written on top. There is a treasure in 
one of the three boxes and it is present in the box with the second largest number on top. Also, to open the box, they need to decode the correct code of this box.
The clue given to them to find the code is that it is the largest number that divides all three given numbers. So, now help Nikitha and Danny to decode the code.

Input Format

Input consists of three integers. The first input corresponds to the number of the first box. The second input corresponds to the number of the second box.
The third input corresponds to the number of the third box.

Output Format

Refer to the sample output.

Sample Input 0
2
4
6

Sample Output 0
The treasure is in the box which has the number 4
The code to open the box is 2

Sample Input 1
7
5
6

Sample Output 1
The treasure is in the box which has the number 6
The code to open the box is 1

Python Code:

def find_treasure_and_code(box1, box2, box3):
    numbers = [box1, box2, box3]
    sorted_numbers = sorted(numbers)
    treasure_box = sorted_numbers[1]
    code = 1
    for i in range(2, treasure_box + 1):
        if all(num % i == 0 for num in numbers):
            code = i
    return treasure_box, code
box1 = int(input())
box2 = int(input())
box3 = int(input())
treasure, code = find_treasure_and_code(box1, box2, box3)
print("The treasure is in the box which has the number", treasure)
print("The code to open the box is", code)
