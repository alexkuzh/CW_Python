let a = [
    'apple',
    'grape',
    'tea',
    'tea111',
    'tea2222'
]

// b = a.slice(1,3)
// b = a.concat([1,'2'],6)
// console.log(b)

// a.forEach((item, index, array)=>{console.log(`${item} имеет позицию ${index} в ${array}`)} )
// console.log(a.indexOf('tea1'))
// console.log(a.lastIndexOf('tea1'))
// a.includes(item, from)

// let arr = [ 1, 2, 15 ];
// arr.sort();
// console.log(arr)
//
// let names = 'Вася';
// let arr  = names.split('')
// console.log(arr)
//
// let st = arr.join(', ')
// console.log(st)


///////////////////////*
//
// for (let i = 0, j=3, arr= [2,4,5]; true; i++) {
//     console.log(i)
// }
// for (выражение 1; выражение 2; выражение 3) {
//     выполняемый блок кода
// }

// do{
//     выполняемый блок кода
// }
// while (условие)

// for (;true;){
//     break
//     continue
//     console.log()
// }

// while (true){}
//
// function makeUser(name, age) {
//     return {
//         name: name,
//         age: age
//         // ...другие свойства
//     };
// }
//
// let user = makeUser("John", 30);
// console.log(user.name)

// let obj = {
//     for: 1,
//     let: 2,
//     return: 3
// };
//
// console.log('for' in obj )

let user = {
    name: "John",
    age: 30,
    isAdmin: true
};

// for (let key in user) {
//     console.log(key)
//     console.log(user[key])
// }

a = 'name'
console.log(user.age,user.name)
console.log(user[a])

delete user.age
console.log(user)
console.log('name' in user)