#Names are given in a file, check whether a particular name is present.



with open("name.txt", "r") as name:
        lines = name.readlines()
        for line in lines:
            if "Rohan" in line:
                print("Rohan is present")
                break
        else:
            print("Rohan is not present")

            


