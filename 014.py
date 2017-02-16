def main():

    even = lambda x: x / 2
    odd  = lambda x: 3 * x + 1

    max_steps = 0
    for x in range(1, 1000000, 1):
        y = x
        step = 1
        while y != 1:
            if y % 2 == 0:
                y = even(y)
            else:
                y = odd(y)
            step += 1

        if step > max_steps:
            max_steps = step
            number = x

    return number


if __name__ == '__main__':
    print(main())
