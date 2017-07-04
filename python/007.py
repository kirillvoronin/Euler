from math import sqrt

def main():

    n = 10001
    numbers = list()
    x = 2

    while len(numbers) != n:
        #print(len(numbers))
        for y in range(2,int(sqrt(x))+1):
            if x % y == 0:
                break
        else:
            numbers.append(x)
        x += 1

    return numbers[-1]

if __name__ == '__main__':
    print(main())
