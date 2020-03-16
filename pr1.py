class student :
     def __init__(self,name,rollno,subject,marks):
         self.name=name
         self.rollno=rollno
         self.subject=subject
         self.marks=marks
    
     def display(self):
         print("Name:",self.name)
         print("Roll No:",self.rollno)
         print("Subject:",self.subject)
         print("marks:",self.marks)
         if (self.marks >= 80):
             print("Your grade is O")
         elif (self.marks >= 60 and self.marks <= 80):
             print("your grade is A")
         elif (self.marks <= 40):
             print("Your grade is F")
   
name=input("Please Enter Your Name:")
rollno=int(input("Please Enter Your Roll No:"))
subject=input("Please Enter A Subject:")
marks=input("Please enter Your Marks:")
s1=student(name,rollno,subject,marks)
s1.display()

