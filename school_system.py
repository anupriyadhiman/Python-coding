#Build a simple school which allows for :: 
# 3.1 Adding a new student to a class with a Name & (unique) ID 
# 3.2 Showing total number of students in a class 
# 3.3 Removing the name of a student from a class 
# 3.4 Promoting a student to the next grade

from base64 import standard_b64decode


def new_student():
    id = int(input("Enter the id of the student : "))
    name = str(input("Enter the name of the student : "))
    standard = int(input("Enter the class of the student : "))
    student_info = {
        "ID" : id,
        "Name" : name,
        "standard" : standard
    }
    return student_info

def total_student(student_info):
    print("Total students in class",student_info["standard"],"is",len(student_info))
    return student_info

def remove_student(student_info):
    id = int(input("Enter the id of the student to be removed : "))
    del student_info[id]
    return student_info

def promote_class(student_info):
    id = int(input("Enter the id of the student to be promoted : "))
    student_info[id]["standard"] = student_info[id]["standard"] + 1
    return student_info

def main():
    student_info = {}
    while True:
        print("1. Add a new student")
        print("2. Show total number of students in a class")
        print("3. Remove the name of a student from a class")
        print("4. Promote a student to the next grade")
        print("5. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            student_info[new_student()["ID"]] = new_student()
        elif choice == 2:
            total_student(student_info)
        elif choice == 3:
            remove_student(student_info)
        elif choice == 4:
            promote_class(student_info)
        elif choice == 5:
            exit()
        else:
            print("Invalid choice")
if __name__ == "__main__":
        main()
