# Miles Philips
# PROG 260
# Searching & Sorting
# 8-9-19

# Import modules.
from binarySearch2 import binarySearch 
import insertionsort

# Create a Student class that has three attributes: LastName, FirstName and Score.
class Student:

    # Initialize 
    def __init__(self, LastName, FirstName, Score):
        self.LastName = LastName
        self.FirstName = FirstName
        self.Score = Score

    # Define string module. 
    def __str__(self):
        return str(self.LastName) + str(self.FirstName)
    
    # Define greater than function. 
    def __gt__(self, other):
        return (self.LastName,self.FirstName) > (other.LastName,other.FirstName) 
    
def main():
    print("Welcome to the Student Score Finder\n\n")

    # List of student names & scores.
    studentData = [["Smith", "Joe", 78], ["Lily", "Sanders", 89], ["Maya","Cooper", 94], ["Joe", "Smith", 67], ["Noble", "Barnes",50], ["Hewlett", "Packard", 88], ["Harerra", "Jose", 95], ["Sally", "Barnes", 77], ["Mary", "Smith", 77], ["Raj", "Sharma", 56]]
    # Sort list.
    studentData.sort()
    # Dispaly sorted list.
    print("Student list in sorted order")
    print() 
    for name in range(0, len(studentData)):
        print(f"Name: {studentData[name][0]} {studentData[name][1]}")
    print()
    # prompts the user for the first and last name of the student they want 
    # to know the score for, performs a search using the Binary Search and prints the score.
    flag = "y"
    while flag.lower() == "y":
        first = input("Please enter student's first name: ")
        last = input("Please enter student's last name: ")
        firstsearch = binarySearch(first,studentData)
        lastsearch = binarySearch(last,studentData)
        if (firstsearch == -1) or (lastsearch == -1):
            print("No student by that name in database")
            flag = input("Continue? (y/n)")
        else:
            print("Score: ",studentData[firstsearch][2])
            flag = input("Continue? (y/n)")

    if flag.lower() != "y" or "n":
        print("Unrecognized command, please try again.") 
        flag = input("Continue? (y/n)")
    
    if flag.lower() ==  "n":
        print("Goodbye!")

if __name__ == "__main__":
    main()
    
    
