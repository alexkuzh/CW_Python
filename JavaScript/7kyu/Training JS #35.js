// https://www.codewars.com/kata/57353de879ccaeb9f8000564
function thinkingAndTesting(number,base){
    //coding here...
    return number - base**Math.floor(Math.log10(number)/Math.log10(base))
}
