Union - Student Details using Union
Write a program to read and display student data using union.

Input Format
The first character input consists of the grade of the student
The second character array input consists of the roll number of student
The third float input consists of the mark of the student
The fourth integer input consists of the fees for student

Output Format
Refer to the sample output

Sample Input 0
A
15EC110
78.98
25000

Sample Output 0
Grade is: A
Rollno is: 15EC110
Mark is: 78.98
Fees paid is: 25000

Sample Input 1
C
15EC089
56
50000

Sample Output 1
Grade is: C
Rollno is: 15EC089
Mark is: 56
Fees paid is: 50000

Python Code:

class Student:
    def __init__(self):
        self.grade = ''
        self.rollno = ''
        self.mark = 0.0
        self.fees = 0
def display_student_data(student):
    print("Grade is:", student.grade)
    print("Rollno is:", student.rollno)
    print("Mark is:", student.mark)
    print("Fees paid is:", student.fees)
student_data = Student()
student_data.grade = input()
student_data.rollno = input()
student_data.mark = input()
student_data.fees = int(input())
display_student_data(student_data)
