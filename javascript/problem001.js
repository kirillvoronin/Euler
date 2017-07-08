/*

Problem: Find the sum of all the multiples of 3 or 5 below 1000.

We can solve this problem with brutforce. 
Computers are powerful and fast, so stuff like that is easy to compute even with brutforce.

int(x) = 999 / 3
int(y) = 995 / 5
int(z) = 990 / 15

int(x) * math.ceil(int(x)/2) * 3 + int(y) * math.ceil(int(y)/2) * 5 - (int(z)+1) * math.ceil(int(z)/2) * 15

*/

/* eslint no-console: ["error", { allow: ["log"] }] */
function getResult() {
  let sum = 0;
  for (let i = 1; i < 1000; i += 1) {
    if ((i % 3 === 0) || (i % 5 === 0)) {
      sum += i;
    }
  }
  return sum;
}

console.log(['result', getResult()].join(': '));
