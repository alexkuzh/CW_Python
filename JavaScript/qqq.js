// function validBraces(braces){
//     a = braces.length+1
//     while (braces.length!=a){
//         a = braces.length
//         console.log(braces)
//         if (braces.indexOf('()')>=0) {braces = braces.replace('()','')}
//         if (braces.indexOf('{}')>=0) {braces = braces.replace('{}','')}
//         if (braces.indexOf('[]')>=0) {braces = braces.replace('[]','')}
//     }
//     return braces.length == 0
// }

// function validBraces(braces){
//     while(braces.indexOf("{}") != -1 || braces.indexOf("()") != -1 || braces.indexOf("[]") != -1){
//         braces = braces.replace("{}", "").replace("()", "").replace("[]", "");
//     }
//     return braces.length == 0;
// }

// function validBraces(braces){
//     for (var i = 0, depth = []; i < braces.length; i++) {
//         switch (braces[i]) {
//             case '(': case '[': case '{': depth.push(braces[i]); break;
//             case ')': if (depth.pop() != '(') return false; break;
//             case ']': if (depth.pop() != '[') return false; break;
//             case '}': if (depth.pop() != '{') return false; break;
//         }
//         console.log(depth)
//     }
//     return depth.length == 0;
// }
//
// console.log(validBraces('[({})]'))

// function expandedForm(num) {
//     let s = String(num)
//     let a = ''
//     for (let i = 0; i < s.length; i++){
//         if (s[i] != '0') {
//             a += s[i].padEnd(s.length-i,'0') + ' + '
//         }
//     }
//     return a.substring(0,a.length-3)
// }

// const expandedForm = n => n.toString()
//     .split("")
//     .reverse()
//     .map( (a, i) => a * Math.pow(10, i))
//     .filter(a => a > 0)
//     .reverse()
//     .join(" + ");
//
// let expandedForm = n => [...String(n)].reverse().map((x,i) => x == '0' ? '' : x + '0'.repeat(i)).filter(x => x != '').reverse().join(' + ')
//
// // console.log('5'.padEnd(5,'0'))
// console.log(expandedForm(70304))

// function f(t) {
//     let a = 0
//     for (x of t){
//         a += x.charCodeAt(0)-96
//     }
//     return a
// }

// function high(x){
//     a = x.split(' ')
//     m = 0
//     w = ''
//     for (n of a){
//         if (m<f(n)){
//             m=f(n);
//             w=n
//         }
//     }
//     return w
// }

// function high(s){
//     let as = s.split(' ').map(s=>[...s].reduce((a,b)=>a+b.charCodeAt(0)-96,0));
//     console.log(as)
//     return s.split(' ')[as.indexOf(Math.max(...as))];
// }
//
// function high(words) {
//     const alpha = ' abcdefghijklmnopqrstuvwxyz';
//     const score = word => word.split('').reduce((a, b) => a + alpha.indexOf(b), 0);
//     return words
//         .split(' ')
//         .map((word, pos) => ({ word: word, pos: pos, score: score(word) }))
//         .sort((a, b) => a.score - b.score || b.pos - a.pos)
//         .pop()
//         .word;
// }
//
// console.log(high('man i need a taxi up to ubud'))

// function f(t) {
//     let r = ''
//     for (let i = 0; i < t.length; i++) {
//         if (i % 2 === 0) {
//             r +=t[i].toUpperCase()
//         } else {
//             r+=t[i].toLowerCase()
//         }
//     }
//     return r
// }
//
// function toWeirdCase(string){
//     a = string.split(' ')
//     let d = []
//     for (x of a) {
//         d.push(f(x))
//     }
//     return d.join(' ')
// }
//
//
// console.log(f("Weird string case"))

// function isValidIP(str) {
//     return str.search(/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/) === 0
// }

// function isValidIP(str) {
//     return /^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$/.test(str);
// }

// function solution(number){
//     // convert the number to a roman numeral
//     s = ''
//     while ( number>0){
//         if (number>=1000){s +='M';number -= 1000;continue}
//         if (number>=900){s +='CM';number -= 900;continue}
//         if (number>=500){s +='D';number -= 500;continue}
//         if (number>=400){s +='CD';number -= 400;continue}
//         if (number>=100){s +='C';number -= 100;continue}
//         if (number>=90){s +='XC';number -= 90;continue}
//         if (number>=50){s +='L';number -= 50;continue}
//         if (number>=40){s +='XL';number -= 40;continue}
//         if (number>=10){s +='X';number -= 10;continue}
//         if (number>=9){s +='IX';number -= 9;continue}
//         if (number>=5){s +='V';number -= 5;continue}
//         if (number>=4){s +='IV';number -= 4;continue}
//         if (number>=1){s +='I';number -= 1;continue}
//     }
//     return s
// }

// function solution(number){
//     var map = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1},
//         output = '';
//
//     for (var i in map ) {
//         while ( number >= map[i] ) {
//             output += i;
//             number -= map[i];
//         }
//     }
//     return output;
// }

// String.prototype.camelCase=function(){
//     //your code here
//     if (this == '') return ''
//     let s = this.split(' ')
//     let a = []
//     for (x of s){
//         a.push(x.charAt(0).toUpperCase() + x.slice(1))
//     }
//     return a.join('')
// }
//
// console.log('camel cDse method'.camelCase())

// function scoreHand(cards) {
//     a = 0
//     count_ace = 0
//     for (x of cards){
//         if (x == "J" || x == "Q" || x == "K") {a+=10}
//         else if (x== "A"){ count_ace++; a+=11}
//         else {a+=parseInt(x)}
//         if (a>21 && count_ace>0){a-=10; count_ace--}
//     }
//     if (a>21 && count_ace>0){a-=10; count_ace--}
//     return a
// }

// const cardsMap = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, J: 10, Q: 10, K: 10, A: 1}
//
// const scoreHand = cards => {
//     const sum = cards.reduce((acc, card) => acc + cardsMap[card], 0)
//     return sum < 12 && cards.includes('A') ? sum + 10 : sum
// }

// function scoreHand(cards)
// {
//     var aces = 0;
//     var total = cards.reduce((t, c) => {
//         switch (c) {
//             case "J":
//             case "Q":
//             case "K": t += 10; break;
//             case "A": t += 11; aces++; break;
//             default:  t += Number(c); break;
//         }
//         return t;
//     },0);
//     while (aces > 0 && total > 21){
//         total -= 10;
//         aces--;
//     }
//     return total;
// }

// function isPrime(number) {
//     if (number <=1) {
//         return false
//     }
//     for (let i = 2; i < number; i++) {
//         if (number % i == 0) {
//             return false
//         }
//     }
//     return true
// }
//
// function getPrimes(start, finish) {
//     let a = []
//     let fin = finish;
//     let st = start
//     if (start > finish) {st = finish;fin = start}
//     for (let i = st; i <= fin; i++) {
//         if (isPrime(i)) {
//             a.push(i)
//         }
//     }
//     return a
// }

// const isPrime = n => {
//     for (let i = 2, s = Math.sqrt(n); i <= s; i++)
//         if (n % i === 0) return false;
//     return n > 1;
// }
//
// const getPrimes = (x, y) => {
//     [x, y] = [x, y].sort((x, y) => x - y);
//     return [...Array(y + 1).keys()].slice(x).filter(isPrime);
// }
