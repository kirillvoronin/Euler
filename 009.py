from math import sqrt

def main():



    for x in range(2,1000+1):
        for y in range(x+1, 1000+1):
            z = sqrt(x**2 + y**2)
            if z.is_integer() and (x+y+z) == 1000:
                return (x*y*z)



if __name__ == '__main__':
    print(main())
