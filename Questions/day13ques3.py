#Marks of a student are given in a file, calculate the average marks.

with open("student.txt", "r") as marks:
        lines = marks.readlines()
        total = 0
        for line in lines:
            total += int(line)
        print("Average marks: ", total / len(lines))
