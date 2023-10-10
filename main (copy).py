'''Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cummulative Grade Point Average) in desending order.
Each students object has the following attributes:
name(string),roll_number(string),and cgpa(float).Test the function with different input lists of students.'''

class Students:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number=roll_number
    self.cgpa=cgpa
    
def sort_students(student_list):
  #sort the list of students in the desending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  return sorted_students
  
#Example usage:
students = [
    Students("Hari", "A123",7.8),
    Students("Srikanth", "A124",8.9),
    Students("Saumya", "A125",9.1),
    Students("Mahidhar", "A126",9.9),
]
  
sorted_students = sort_students(students)
                                 
  #print the sorted list of the students
for student in sorted_students:
    print("Name: {},Roll Number: {}, CGPA:{}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))