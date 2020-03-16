// https://www.codewars.com/kata/5721c189cdd71194c1000b9b
function grabDoll(dolls){
    var bag=[];
    //coding here
    for (x of dolls){
        if ((x == 'Hello Kitty') || (x == 'Barbie doll')){
            bag.push(x);
            if (bag.length >= 3) break;
        }
        else continue;
    }
    return bag;
}
