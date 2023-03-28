// regexp = new RegExp("шаблон", "флаги");
// regexp = /шаблон/; // без флагов
// regexp = /шаблон/gmi;
// i - A a
// g - global
// m - multystring
// s - . \n
//u - unicode support
// y - position

let s = 'asdasd Home sweet home homelander'
let patt = 'home'
let flags = 'gi'
reg = new RegExp(patt, flags);
// let a = s.matchAll(reg)
// console.log(Array.from(a)[2].index)
// for (x of a){
//     console.log(x)
// }

// console.log('123, 345, 67'.split(/,/))

// console.log(s.search(reg))

// console.log(s.match(/home1/gi))

// s.replace(reg,replasment)
// console.log(s.replace(/home/gi,"$$One"))
// console.log(reg.test(s))

// g, i, m, u, s, y
console.log(reg.lastIndex)
console.log(reg.exec(s))
console.log(reg.lastIndex)
console.log(reg.exec(s))

https://habr.com/ru/post/349860/#Regulyarki