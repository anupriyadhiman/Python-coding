#solve the fizzbuzz problem 

def callfunc():
    for i in range(1, 101):         
     if i%5 == 0 and i%3 == 0:
         print('Fizzbuzz')
     elif i%5 == 0:
         print('Buzz')
     elif i%3 == 0:
         print('fizz')
     else:
        print(i)

if __name__ == '__main__':
   callfunc()