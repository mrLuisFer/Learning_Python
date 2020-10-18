#!/bin/python3

# Complete the 'fizzBuzz' function below.
# The function accepts INTEGER n as parameter.

def fizzBuzz(x):
    # Write your code here
    s = x + 1
    for s in range(1,s):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
            continue
        elif n % 3 == 0:
            print('Fizz')
            continue
        elif n % 5 == 0:
            print('Buzz')
            continue
        print(n)
    
        
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
