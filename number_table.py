def callfunc():
    print("Enter number that you want to see table of : ")
    n = int(input())
    for i in range(1, 11):
        table = i*n
        print(table)


if __name__ == '__main__':
   callfunc()