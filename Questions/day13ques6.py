#Given a file with numbers , calculate mean, median and mode
with open("student.txt", "r") as marks:
        lines = marks.readlines()
        total = 0
        for line in lines:
            line = int(line)
            total += int(line)
        print("Mean: ", total / len(lines))
        lines.sort()
        print("Median: ", lines[len(lines) // 2])
        print("Mode: ", max(set(lines), key = lines.count))