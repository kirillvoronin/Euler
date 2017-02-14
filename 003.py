from math import sqrt

# used brute force method

def main():
    n = 600851475143
    maximum = 0
    for x in range(2,int(sqrt(n))):
        if n % x == 0:
            isPrime = True
            for y in range(2,x-1):
                if x % y == 0:
                    isPrime = False
            if isPrime:
                maximum = x

    return maximum




if __name__ == '__main__':
    print(main())
