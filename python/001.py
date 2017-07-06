"""

Problem: Find the sum of all the multiples of 3 or 5 below 1000.

We can solve this problem with brutforce. 
Computers are powerful and fast, so stuff like that is easy to compute even with brutforce.

int(x) = 999 / 3
int(y) = 995 / 5
int(z) = 990 / 15

int(x) * math.ceil(int(x)/2) * 3 + int(y) * math.ceil(int(y)/2) * 5 - (int(z)+1) * math.ceil(int(z)/2) * 15

"""


def main():
    return sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))


if __name__ == '__main__':
    print(main())
