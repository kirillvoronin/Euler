

def main():
    x = 1
    y = 1
    summ = 0
    result = 0
    while result < 4000000:
        if x % 2 == 0:
            summ += x

        result = x + y
        y = x
        x = result

    return summ


if __name__ == '__main__':
    print(main())
