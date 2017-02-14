

def main():

    sum_x, sum_y = 0,0
    for x in range(11):
        sum_x += x*x
    for y in range(11):
        sum_y += y

    print(sum_y*sum_y - sum_x)


if __name__ == '__main__':
    main()
