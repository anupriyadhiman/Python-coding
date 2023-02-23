#Given a file with strings, calculate the permutations.

with open("string.txt", "r") as string:
        lines = string.readlines()
        for line in lines:
            print("Permutations of ", line, "are: ")
            for i in range(len(line)):
                print(line[i], line[i + 1], line[i + 2])
            


            


        