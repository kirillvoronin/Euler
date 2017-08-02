
def main():
    for x in range(2,1000 + 1):
        for y in range(x + 1, 1000 + 1):
            z = 1000 - (x+y)
            if (x + y + z) == 1000 and (x ** 2 + y ** 2 == z ** 2):
                return (x * y * z)



if __name__ == '__main__':
    print(main())
