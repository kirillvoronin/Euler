let number = 600851475143;
let res;
let primer = true;
const sqrtFromNumber = Math.sqrt(number);

for (let i=3; i<=sqrtFromNumber; i+=2) {
  if (number % i === 0) {
    primer = true;
    for (let j=3; j<=Math.sqrt(i); j+=2) {
      if (i % j === 0) {
        primer = false;
        break;
      }
    }
    if (primer) {
      res = i;
    }
  }
}

console.log(res);