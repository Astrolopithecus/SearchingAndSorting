from insertionsort import insertionSort
from binarySearch import binarySearch2
class Student: 
    def __init__(self, first, last, score):
        self.firstName = first
        self.lastName = last
        self.score = score
    
    def __str__(self):
        return f"Name: {self.firstName} {self.lastName}"
    def __eq__(self, other):
        return self.firstName.lower() == other.firstName.lower() and self.lastName.lower() == other.lastName.lower()
    
    def __lt__(self, other):
        return self.firstName < other.firstName.lower() if self.lastName.lower() == other.lastName.lower() else self.lastName.lower() < other.lastName.lower()

def main():
    print("\nWelcome to the Student score locator\n")
    studentsList = [Student("Smith", "Joe", 78),
    Student("Lily", "Sanders", 89),
    Student("Maya","Cooper", 94),
    Student("John", "Smith", 67),
    Student("Noble", "Barnes",50),
    Student("Hewlett", "Packard", 88),
    Student("Harerra", "Jose", 95),
    Student("Sally", "Barnes", 77),
    Student("Mary", "Smith", 77),
    Student("John", "Doe", 83),
    Student("Raj", "Sharma", 56)]

    insertionSort(studentsList)
    print("Students list in sorted order")
    for s in studentsList:
        print(s)
    
    print()
    ans = 'y'
    while (ans.lower() == 'y'):
        first = input("Please enter Student's first name: ")
        last = input("Please enter Student's last name: ")
        index = binarySearch2(Student(first, last, 0), studentsList)
        if (index >= 0):
            print("Score: ", studentsList[index].score)
        else:
            print("No student by that name")

        ans = input("Continue?(y/n) ")
        
    
    print("Goodbye")

    
if (__name__ == "__main__"):
    main()
