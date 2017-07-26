"""
Euler problem num 55

A Lychrel number is a natural number that cannot
    form a palindrome through the iterative process of repeatedly reversing
        its digits and adding the resulting numbers.

This process is sometimes called the 196-algorithm,
    after the most famous number associated with the process.

Q: How many Lychrel numbers are there below ten-thousand?
"""


def isPalindrome(x):
    return str(x) == str(x)[::-1]


def isLychrel(x):
    for i in range(50):
        x += int(str(x)[::-1])
        if isPalindrome(x):
            return False
    return True


def main():
    result = sum(1 for x in range(10000) if isLychrel(x))
    return str(result)


if __name__ == "__main__":
    print(main())
