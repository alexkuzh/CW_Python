// https://www.codewars.com/kata/571f1eb77e8954a812000837
function animal(obj){
    return 'This ' + obj.color + ' ' + obj.name + ' has ' + obj.legs + ' legs.';
}
console.log(animal({name:"dog",legs:4,color:"white"}));

function animal1(obj){
    return obj.name + ' ' + obj.legs + ' ' + obj.color
}

let obj = {name:"dog",legs:4,color:"white"}

console.log(animal({name:"dog",legs:4,color:"white"}))