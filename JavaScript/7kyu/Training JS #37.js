// https://www.codewars.com/kata/5735e39313c205fe39001173
function countAnimals(animals,count){
    a = []
    for (let x of count){
        a.push((animals.match(new RegExp(x,"g"))||[]).length)
    }
    return a
}