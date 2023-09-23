
class Students:
  def_init_(self, name, roll_number, CGPA) :
  self. name=name
  self. roll_number=roll_number
  self. CGPA=CGPA
def sort_students (students_list) :
sorted_students=sorted(students_list, key=lambda students:students.cgpa, reverse=ture)
return sorted_students
students=[
students ("hari", "A123", 7.8), 
students (" srikanth", A124", 8.4), 
students ("sowmiya", "A125", 9.1), 
students (" mani", "A126", 9.9) 
]
sorted_students=sort_students (students)for students in sorted_students:
print(" num:{}, rollnumber:{}, CGPA:{}".format(students.name, students. roll_number, students. cgpa))