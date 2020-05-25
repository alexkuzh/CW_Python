// https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
function factorial(n)
{
    if ((n<0) || (n>12)) {throw new RangeError("RangeError")}
    let rval=1;
    for (let i = 2; i <= n; i++)
        rval = rval * i;
    return rval;
}

console.log(factorial(-100))