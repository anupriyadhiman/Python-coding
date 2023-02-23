def callfunc():
    dishes = ['pizza', 'pasta', 'indian thali', 'Hamburger']
    print("Enter the dish number that you want to order \n 1 : pizza \n 2 : pasta \n 3 : indian thali \n 4 : Hamburger")
    a = int(input())
    print(dishes[a-1])

if __name__ == '__main__':
   callfunc()