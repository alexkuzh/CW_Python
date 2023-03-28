let i = 0;
let id = setInterval(
    function any(){
        i++;
        console.log("Прошло " + i + " сек.");
        if(i == 5){
            clearInterval(id);
        }
    },
    1000);

let i1 = 0;
let id1 = setTimeout(
    function any(){
        console.log("Прошлa " + 1 + " сек.");
        clearTimeout(id1)
    },
    1000);


// let id = setInterval(any,1000);