class Student:
    name=""
    marks=""

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def StudentDetails(self):
        print(" Student name is ",self.name," and  Marks ",self.marks)
        if self.marks>=80:
            print(self.name,"Got Grade A ")
        elif self.marks>=60:
            print(self.name,"Got Grade B ")
        elif self.marks<60:
            print(self.name,"Got Grade C ")

s1=Student("Ali",85)
s2=Student("Sara",62)
s3=Student("Zaid",45)
s4=Student("Hussnain",95)

s1.StudentDetails()
s2.StudentDetails()
s3.StudentDetails()
s4.StudentDetails()