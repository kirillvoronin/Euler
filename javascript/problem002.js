/* eslint no-console: ["error", { allow: ["log"] }] */
function getResult(first, second) {
  let currVal = first || 1;
  let nextVal = second || 2;
  let sum = 0;
  while (currVal <= 4000000) {
    if (currVal % 2 === 0) {
      sum += currVal;
    }
    nextVal += currVal;
    currVal = nextVal - currVal;
    console.log(['curr will be', currVal].join(': '));
    console.log(['next will be', nextVal].join(': '));
  }
  return sum;
}

console.log(['result', getResult()].join(': '));
