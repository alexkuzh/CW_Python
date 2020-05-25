// https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/javascript
function removeDuplicateWords (s) {
   return [...new Set(s.split(' '))].join(' ')
}


console.log(removeDuplicateWords('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))