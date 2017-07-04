from math import sqrt

def main():
    x = 1
    triangle = [1]
    while True:

        triangle.append(x+1)
        x += 1
        res = sum(triangle[0:x])
        deli = 0

        for y in range(1,int(sqrt(res))):
            if res % y == 0: deli += 2

        if deli > 500: break

    return res

if __name__ == '__main__':
    print(main())
