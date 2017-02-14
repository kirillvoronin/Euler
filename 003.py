import math


def main():
    n = 600851475143
    #n = 13195
    maximum = 0
    for x in range(2,int(math.sqrt(n))):
        if n % x == 0:
            divs = 0
            for y in range(2,x-1):
                if x % y == 0:
                    divs += 1
            if divs == 0:
                if x > maximum:
                    maximum = x

    return maximum




if __name__ == '__main__':
    print(main())
