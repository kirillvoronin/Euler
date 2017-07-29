"""

Q: Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

"""

def main(): 
    return max(sum(int(x) for x in str(y ** z)) for y in range(100) for z in range(100))

if __name__ == "__main__":
    print(main())
