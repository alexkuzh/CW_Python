// // // if ?
// // let a = 20
// // if (a < 20)  {
// //     console.log('мало')
// // }
// // else if (a > 20 ){
// //     console.log('много')
// // }
// // else if (a == 20){
// //     console.log('точно')
// // }
//
// // ?
// // let accessAllowed;
// // let age = 6;
// //
// // if (age >18){
// //     accessAllowed = true;
// // } else {
// //     accessAllowed = false;
// // }
// // console.log(accessAllowed)
//
// // let result = условие ? значение1 : значение 2
//
// // accessAllowed  = age >18 ? true : false
//
// // console.log(age >18)
//
// // let age  = 180
// // let message = (age < 3) ? 'hi baby':
// //     (age < 18) ? 'hi teen':
// //         (age == 18)? 'hi' :
// //             'hello'
// //
// // console.log(message)
// // let a = 'message_1';
// // (a == 'message_1') ? console.log('true11111') : console.log('false11111')
// //
// // if (a == 'message_1'){
// //     console.log('true11111')
// // }
// // else {
// //     console.log('false11111')
// // }
// //
// // if (''){
// //     console.log('*********')
// // }
// //
// // if (0){
// //     console.log('*********')
// // }
// //
// //
// // switch (выражение) {
// //     case n:
// //         code block
// //         break;
// //     case n1:
// //         code block
// //         break;
// //     case n2:
// //         code block
// //         break;
// //     case n3:
// //         code block
// //         break;
// //     case n_n:
// //         code block
// //         break;
// //     default:
// //         code block
// // }
// // switch (new Date().getDay()) {
// //     case 0:
// //         day = "Воскресенье";
// //         break;
// //     case 1:
// //         day = "Понедельник";
// //         break;
// //     case 2:
// //         day = "Вторник";
// //         break;
// //     case 3:
// //         day = "Среда";
// //         break;
// //     case 4:
// //         day = "Четверг";
// //         break;
// //     case 5:
// //         day = "Пятница";
// //         break;
// //     default:
// //         day = "Суббота";
// //
// // }
// // switch (new Date().getDay()) {
// //     default:
// //         text = "Будем ждать выходных";
// //         break;
// //     case 6:
// //         text = "Сегодня суббота";
// //         break;
// //     case 0:
// //         text = "Сегодня воскресенье";
// //         // break;
// // }
// switch (new Date().getDay()) {
//     case 4:
//     case 5:
//         text = "Скоро выходные";
//         break;
//     case 0:
//     case 6:
//         text = "Сегодня выходной";
//         break;
//     default:
//         text = "Будем ждать выходных";
// }
// console.log(text)
//
//
//
//
//
//

// || (ИЛИ), && (И) и ! (НЕ)

// let a = true
// let b = false
// result = a || b
// console.log(result)

// ( true || true );   // true
// ( false || true );  // true
// ( true || false );  // true
// ( false || false ); // false

// if (1 || 0) { // работает как if( true || false )
//     console.log('truuuu')
// }

// let hour = 9;
// let isweekend = true
// if (hour < 10 || hour > 18 || isweekend) {
//     console.log('office is closed')
// }

// result = value1 || value2 || value3;

// console.log(0||''||10>20)

// let currentUser = null;
// let defaultUser = "";
//
// let name = currentUser || defaultUser || "unnamed";
//
// console.log(name)

// let x;
//
// false || (x = 23);
//
// console.log(x)

// &&
// result = a && b;
// true && true // true
// true && false // false
// false && true // false
// false && false // false

// let hour = 12;
// let minute = 30;
//
// if (hour == 12 && minute == 30){
//     console.log('The time is 12:30')
// }
//
// if (112 && 10){
//     console.log('truuu')
// }
// else{
//     console.log('falseee')
// }

// result = value1 && value2 && value3;

// console.log(1&&0)
// console.log(1&&5)
// console.log( 1 && 2 && 4 && 5 )
// let a = 0
// let b = 1
// let c = 1
// let d = 1
// console.log(a && (b || c) && d) // false

// let x = 2;
// (x>1) && console.log('больше 0')

// result = !value
// console.log(!!'ffff')
// console.log(Boolean('ffff'))

// let arr = new Array();
let a = []