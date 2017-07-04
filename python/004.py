def main():

    maximum = 0

    for x in range(999,100, -1):
        for y in range(999, 100, -1):
            p = x*y
            if p > maximum:
                n = str(p)
                if n == n[::-1]:
                    maximum = p

    return maximum


if __name__ == '__main__':
    print(main())
