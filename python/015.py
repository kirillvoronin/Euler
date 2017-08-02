def main():
    gridSize = 20
    ways = 1
    for x in range(gridSize):
        ways = ways * ((2 * gridSize) - x)/(x + 1)

    return int(ways)

if __name__ == '__main__':
    print(main())
