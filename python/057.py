from math import log10

"""

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

Q: In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
=>
-- 1 + 1/2 = 3/2 = 1.5
-- 1 + 1/(2 + 1/2) = 7/5 = 1.4
=>
3/2 ; 7/5 ; 17/12 ; 41/29
=> so we getting from sequence this formulae 
=> n(k+1) = n(k) + 2d(k) and 
   d(k+1) = n(k) + d(k), where n is the numerator, d is the denominator
   
"""

from math import log10


def main(limit, denominator, numerator):
  result = 0
  for _ in range(1, limit):
    numerator += (2 * denominator)
    denominator = numerator - denominator
    if int(log10(numerator)) > int(log10(denominator)):
      result += 1
      
  return result
      
if __name__ == "__main__":
  print(main(limit=1000, denominator=2, numerator=3))
