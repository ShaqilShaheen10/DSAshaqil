Grade Problem
Implement a Student class and a Grade class. The Grade class should have two public members:
1. string subject_name
2. char grade

The Student class should have three public members:
1. int student_id
2. string sudent_name
3. vector of Grades grades

The locked code stubs will instantiate a Student object and will check the proper implementation

Sample Input For Custom Testing

Function→ student_id = 1,

student_name 'Julia'=1

1 Julia
2
→ subjectsCount = 2
Physics A → first subject_name
'Physics' first grade ='A'
Chemistry C second subject_name 'Chemistry' second grade = 'C'

Sample Output
1 Julia
Physics A
Chemistry C


Program Code:

#include <iostream>
#include <vector>
#include <string>

class Grade {
public:
    std::string subject_name;
    char grade;
    
    Grade(std::string subject, char g) : subject_name(subject), grade(g) {}
};

class Student {
public:
    int student_id;
    std::string student_name;
    std::vector<Grade> grades;
    
    Student(int id, std::string name, std::vector<Grade> g) : student_id(id), student_name(name), grades(g) {}
    
    void display() {
        std::cout << student_id << " " << student_name << std::endl;
        for(const auto& grade : grades) {
            std::cout << grade.subject_name << " " << grade.grade << std::endl;
        }
    }
};

int main() {
    int student_id = 1;
    std::string student_name = "Julia";
    std::vector<Grade> grades = {Grade("Physics", 'A'), Grade("Chemistry", 'C')};
    
    Student student(student_id, student_name, grades);
    student.display();
    
    return 0;
}
