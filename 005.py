def main():

    num = 2520
    dividers = set([11, 13, 14, 16, 17, 18, 19, 20])
    while True:
        print(num)

        if all(num % x == 0 for x in dividers):
            return(num)

        num += 20

if __name__ == '__main__':
    main()
