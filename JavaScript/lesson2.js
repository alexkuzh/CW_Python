// function sumDigits(number) {
//     let a = 0
//     number = Math.abs(number)
//     while (number>9){
//         a +=number%10
//         number  = Math.floor(number/10)
//     }
//     return a+number
// }

// function sumDigits(number) {
//     return Math.abs(number).toString().split('').reduce(function(a,b){return +a + +b}, 0);
// }

// function sumDigits(number) {
//     return number.toString().split("").reduce(function(sum,n) {
//         return n === '-' ? sum : sum+parseInt(n);
//     },0);
// // }
//
// console.log(sumDigits(99))

// function showSequence(count) {
//         if (count < 0) { return  count + '<0'}
//         if (count == 0) { return '0=0'}
//         // let s = ''
//         let s  = []
//         let a = 0
//         // for (let i=0; i<count; i++){
//         for (let i=0; i<=count; i++){
//             // s += i.toString()+'+'
//             s.push(i)
//             a += i
//         }
//         a += count
//         // s+= count.toString() +' = '+a.toString()
//         let d = s.join('+') +' = '+a.toString()
//         return d //s
// //     }
//
// console.log(showSequence(6))

// function findSum(n) {
//     a = 0
//     for (i=3; i<=n; i++){
//         if (i%3 == 0 || i%5 == 0){ a+=i}
//     }
//     return a
// }

// function findSum(n) {
//     var sum = 0;
//     for (var i = 0; i <= n / 5; i++) {
//         sum += i * 5;
//     }
//     for (var i = 0; i <= n / 3; i++) {
//         sum += i * 3;
//     }
//     for (var i = 0; i <= n / 15; i++) {
//         sum -= i * 15;
//     }
//     return sum;
// }

// const sumMultiples = (m, n) => {
//     let x = n / m | 0;
//     return m * x * (x + 1) / 2;
// };
// const findSum = n =>
//     sumMultiples(3, n) + sumMultiples(5, n) - sumMultiples(15, n);
//
//
// console.log(findSum(10))


// String.prototype.toAlternatingCase = function () {
//     // Define your method here :)
//     let output = "";
//
//     for (let i = 0; i < this.length; i++) {
//
//         var ch = this[i];
//
//         if (ch === ch.toUpperCase()) {
//             output += ch.toLowerCase();
//         } else {
//             output += ch.toUpperCase();
//         }
//     }
//
//     return output;
// }

// String.prototype.toAlternatingCase = function () {
//     return this.split("").map(a => a === a.toUpperCase()? a.toLowerCase(): a.toUpperCase()).join('')
// }
//
// console.log("helloASDASD".toAlternatingCase())


// const rps = (p1, p2) => {
// function rps(p1,p2){
//     if (p1 == p2) return 'Draw!';
//     if ((p1 == 'rock' && p2 == 'scissors')
//         || (p1 == 'scissors' && p2 == 'paper')
//         || (p1 == 'paper' && p2 == 'rock'))
//         return 'Player 1 won!';
//     return 'Player 2 won!';
// };
// const rps = (p1, p2) => {
//     if (p1 === p2) return "Draw!";
//     var rules = {rock: "scissors", paper: "rock", scissors: "paper"};
//     if (p2 === rules[p1]) {
//         return "Player 1 won!";
//     }
//     else {
//         return "Player 2 won!";
//     }
// };

// const rps = (p1, p2) => {
//     if(p1 === p2) {
//         return 'Draw!'
//     };
//     return `Player ${/rockscissors|scissorspaper|paperrock/.test(p1+p2)? 1 : 2} won!`;
// }

// const rps = (p1, p2) => {
//     var map = {
//         'rock': 'scissors',
//         'scissors': 'paper',
//         'paper': 'rock'
//     };
//
//     if (p1 == p2) {
//         return 'Draw!';
//     } else {
//         return 'Player ' + (map[p1] == p2 ? 1 : 2) + ' won!';
//     }
// };

// console.log(rps('scissors','paper'))

// function bmi(weight, height) {
//     let bmi = weight / (height ** 2)
//     if (bmi > 30) {return "Obese"}
//     if (bmi <= 18.5){ return "Underweight"}
//     if (bmi <= 25.0) {return "Normal"}
//     if (bmi <= 30.0) {return "Overweight"}
// }

// function bmi(weight, height) {
//     var formula = (weight / Math.pow(height, 2));
//     switch (true) {
//         case formula <=18.5:
//             return 'Underweight';
//         case formula <=25.0:
//             return 'Normal';
//         case formula <=30:
//             return 'Overweight';
//         default:
//             return 'Obese';
//
//     }
// }
//
// console.log(bmi(80,180))

// function getAverage(marks){
//     return  Math.floor(marks.reduce((a, b) => a + b, 0) / marks.length)
// }

// function getAverage(marks){
//     var sum = 0;
//
//     for (var i in marks)
//         sum += marks[i];
//
//     return parseInt(sum / marks.length);
// }
// console.log(getAverage([2,3,4,5,3]))


// function hero(bullets, dragons){
// //Get Coding!
//     return bullets >= dragons*2
// //     return (bullets / 2 >= dragons) ? true : false;
// }

// function removeExclamationMarks(s) {
//     while (s.search('!')>=0){
//         s = s.replace('!','')
//     }
//     return s
// }
// function removeExclamationMarks(s) {
//     return s.split('!').join('');
// }
// function removeExclamationMarks(s) {
//     return s.replace(/!/g, '');
// }
// console.log(removeExclamationMarks('asda!!@asdas!@'))

// const sequenceSum = (begin, end, step) => {
//     // May the Force be with you
//     let a = 0
//     for (i =begin; i <=end; i+=step){
//         a +=i
//     }
//     return a
// };

// function noOdds( values ){
//     a = []
//     for (x of values)
//         if (x%2 == 0) {a.push(x)}
//     return a
// }
// function noOdds( values ){
//     return values.filter(x => (!x % 2));
// }

// function alienLanguage(str){
//     let a = ''
//     let s = str.toUpperCase().split(' ');
//     for (x of s){
//         a = a = + x.slice(0,x.length-1) + x[x.length -1].toLowerCase() + ' '
//     }
//     return a.trim()
// }
//
// function alienLanguage(str){
//     var words = str.toUpperCase();
//     var sentence = words.split(" ");
//     let s = []
//     for(var wI = 0; wI < sentence.length; wI++) {
//         var newWord = [];
//         for (var cI = 0; cI < sentence[wI].length-1; cI++) {
//             newWord.push(sentance[wI][cI]);
//         }
//         newWord.push(sentence[wI][cI].toLowerCase());
//         s.push(newWord.join(''))
//     }
//     console.log(s.join(' '));
// }
// function nbDig(n, d) {
//     let s = ''
//     for (let x = 0; x<=n; x ++){
//         s +=(x**2).toString()
//     }
//     return s.split(d).length-1
// }
// console.log(nbDig(5750,0))

// function arithmetic(a, b, operator){
//     switch(operator) {
//         case 'add':
//             return a + b;
//         case 'subtract':
//             return a - b;
//         case 'multiply':
//             return a * b;
//         case 'divide':
//             return a / b;
//     }
// }

// function arithmetic(a, b, operator){
//     let arr = {"add":"+", "subtract":"-", "divide":"/", "multiply":"*"}
//     return eval(a.toString()+arr[operator]+b.toString())
// }
//
// console.log(eval('1+2'))