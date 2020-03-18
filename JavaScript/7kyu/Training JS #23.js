// https://www.codewars.com/kata/572af273a3af3836660014a1
function infiniteLoop(in_arr,d,n){
    let k = 0;
    for (let x of in_arr){k = k + x.length};
    if (d == 'left'){
        for (let m = 0; m < n%k; m ++) {
            /* shift left*/
            for (let i = 0; i < in_arr.length - 1; i++) {
                in_arr[i].push(in_arr[i + 1].shift())
            }
            in_arr[in_arr.length - 1].push(in_arr[0].shift())
        }
    }
    if (d == 'right') {
        for (let m = 0; m < n%k; m++) {
            /*shift right*/
            for (let i = 1; i < in_arr.length; i++) {
                in_arr[i].unshift(in_arr[i - 1].pop())
            }
            in_arr[0].unshift(in_arr[in_arr.length - 1].pop())
        }
    }
    return in_arr
}