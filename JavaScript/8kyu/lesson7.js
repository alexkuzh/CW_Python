let m = new Map();
// m.set(key, value)
// m.get(key)
// m.has(key)
// m.delete(key)
// m.clear()
// m.size
m.set("1","str1");
m.set(true,'boolean1')
m.set(1,'num1')
// //
// // // console.log(m.get(1))
// // // console.log(m.get("1"))
// //
// // let john = { name: "John" };
// // let count = new Map();
// // count.set(john,111)
// // console.log(count.get(john))
//
// // map.keys()
// // map.values()
// //map.entries()
//
// for (x of m.entries()){
//     console.log(x)
// }

// m.forEach(((value, key, map) => {
//     console.log(map)
// }))
//
// a = [1,2,3,4,4,2,1]
// console.log(Array.from(new Set(a)))
//

function showName(a,b){
    if (a+b > 0)
        return         'number is positive'
    else {
        // return;
    }

}

console.log(showMessage(2,-3))

// getNumber
// calcValue
// createLastName
// checkAddress


function имя(параметры, через, запятую) {
    /* тело, код функции */
    return
}


function ask(question, yes, no) {
    if (confirm(question)) yes()
    else no();
}

function showOk() {
    alert( "Вы согласны." );
}

function showCancel() {
    alert( "Вы отменили выполнение." );
}

// использование: функции showOk, showCancel передаются в качестве аргументов ask
ask("Вы согласны?", showOk, showCancel);