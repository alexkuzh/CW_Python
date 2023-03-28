// function isPowerOfTwo(n){
//     return Number.isInteger(Math.log2(n));
// }
//
// function isPowerOfTwo(x){
//     return (
//         x == 1 || x == 2 || x == 4 || x == 8 || x == 16 || x == 32 ||
//         x == 64 || x == 128 || x == 256 || x == 512 || x == 1024 ||
//         x == 2048 || x == 4096 || x == 8192 || x == 16384 ||
//         x == 32768 || x == 65536 || x == 131072 || x == 262144 ||
//         x == 524288 || x == 1048576 || x == 2097152 ||
//         x == 4194304 || x == 8388608 || x == 16777216 ||
//         x == 33554432 || x == 67108864 || x == 134217728 ||
//         x == 268435456 || x == 536870912 || x == 1073741824 ||
//         x == 2147483648);
// }
//
// function isPowerOfTwo(n) {
//     return n === 0 ? false : (n & (n - 1)) == 0
// }
//
// function isPowerOfTwo(n){
//     return /^10*$/.test(n.toString(2));
// }
//
// function isPowerOfTwo(n){
//     if(n<2) return false;
//     if(n==2) return true;
//     if(n>2) return isPowerOfTwo(n/2);
// }

// function factorial(n) {
//     if (n < 0 || n > 12)
//         throw RangeError();
//     var f = 1;
//     while (n > 1)
//         f *= n--;
//     return f;
// }
//
// function factorial(n)
// {
//     if(n < 0 || n > 12) throw new RangeError('Ошибка');
//     return n ? n * factorial(n-1) : 1;
// }
//
// number([]) // => []
// number(["a", "b", "c"]) // => ["1: a", "2: b", "3: c"]

// var number = function(array) {
//     return array.map(function (line, index) {
//         return (index + 1) + ": " + line;
//     });
// }
//
// let number = (a) => a.map((v, i) => `${i + 1}: ${v}`)

// describeAge=age=>"You're a(n) " + ((age <= 12)?"kid":(age >= 13 && age <= 17)?"teenager":(age >= 18 && age <= 64)?"adult":"elderly")

// function a(age){
//     return (age <= 12) ?
//     "You're a(n) kid":(age >= 13 && age <= 17) ?
//     "You're a(n) teenager": (age >= 18 && age <= 64) ?
//     ("You're a(n) adult"):"You're a(n) elderly"
// }
//
// console.log(a(15))

// function getDivisorsCnt(n){
//     let a = new Set()
//     if (n == 1) {return 1}
//     for (start = 1; start <n; start ++){
//         if (n % start == 0)
//         {
//             a.add(n/start)
//             a.add(start)
//         }
//     }
//     return a.size
// }

// function getDivisorsCnt(n) {
//     for (var d = 0, i = n; i > 0; i--) {
//         if (n % i == 0) d++;
//     }
//     return d;
// }

// function evaporator(content, evap_per_day, threshold){
//     d = 0
//     content = 100
//     while (content>threshold){
//         d +=1
//         content = content * (1-evap_per_day/100)
//     }
//     return d
// }
//
// function evaporator(cont, epd, thr){
//     var n = 0;
//     for(var q=100; q > thr; q -= epd*q/100){
//         n++;
//     }
//     return n;
// }

// function mxdiflg(a1, a2) {
//     if (a1.length ==0 || a2.length==0) { return -1}
//     console.log(a1)
//     console.log(a2)
//     a1.sort(function(a, b){return a.length-b.length})
//     a2.sort(function(a, b){return a.length-b.length})
//     let a1_min = a1[0].length
//     let a2_min = a2[0].length
//     let a1_max = a1[a1.length-1].length
//     let a2_max = a2[a2.length-1].length
//
//     if (a1.length == 1 && a2.length == 1) {return Math.abs(a1_min-a2_min)}
//     return Math.max(Math.abs(a1_min - a2_max), Math.abs(a1_max - a2_min))
// }
//
// function mxdiflg(arr1, arr2) {
//     if (arr1.length == 0 || arr2.length == 0) { return -1; };
//     var diffA = maxLen(arr1) - minLen(arr2), diffB = maxLen(arr2) - minLen(arr1);
//     return diffA > diffB ? diffA : diffB;
// }
//
// function minLen(array) {
//     return array.sort(function (a, b) { return a.length - b.length;})[0].length;
// }

// function minValue(values){
//     values.sort()
//     s = new Set(values)
//     a = []
//     for (x of s){
//         a.push(x)
//     }
//     return +a.join('')
// }
//
// function minValue(values){
//     let arr = Array.from(new Set(values))
//     return parseInt(arr.sort().join(''))
// }
//
// const minValue = (v) => +[...new Set(v)].sort().join``
//
// console.log(minValue([1,4,3,2,2,2,2]))

// function isLeapYear(year) {
//     return (year % 100 !== 0 && year % 4 === 0) || year % 400 === 0;
// }
//
// function isLeapYear(year) {
//     if(0 == year%400) return true;
//     if(0 == year%100) return false;
//     if(0 == year%4) return true;
//
//     return false;
// }

// function solution(nums){
//     return nums.sort(function(a1, b2){
//         return a1 - b2
//     });
// }

// function twoOldestAges(ages){
//     ages.sort(function(a, b){return b - a});
//     console.log(ages)
//     return [ages[1],ages[0]]
// }
//
// function twoOldestAges(ages){
//     return ages.sort(function(a,b){return a-b;}).slice(-2);
// }

//
// function twoOldestAges(ages){
//     return ages.sort().slice(-2);
// }
//
// console.log(twoOldestAges([2,4,3,2,1,8,6]))
//
// function sortByLength (array) {
//     // return array.sort(function(a, b){return b.length-a.length})
//     return array.sort()
// };

let sortByLength = arr => arr.sort();

console.log(sortByLength(["Telescopes", "Glasses", "Eyes", "Monocles"]))