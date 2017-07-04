const number = 600851475143;
const sqrtFromNumber = Math.sqrt(number);
let res;
let isPrime = true;

for (let i=3; i<=sqrtFromNumber; i+=2) {
  if (number % i === 0) {
    isPrime = true;
    for (let j=3; j<=Math.sqrt(i); j+=2) {
      if (i % j === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      res = i;
    }
  }
}

console.log(res);
