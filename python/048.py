# -*- coding: utf-8 -*-

def main():

    summ = sum(x**x for x in range(1,1000))

    return (str(summ)[-10:])


if __name__ == '__main__':
    print(main())
