// https://www.codewars.com/kata/5735956413c2054a680009ec
function rndCode(){
    //coding here...
    let chars = 'ABCDEFGHIJKLM'
    let num = '0123456789'
    let symb = '~!@#$%^&*'
    let s = ''
    for (let i=0;i<2;i++){s = s+chars.substr(chars.length*Math.random(),1)}
    for (let i=0;i<4;i++){s = s+num.substr(num.length*Math.random(),1)}
    for (let i=0;i<2;i++){s = s+symb.substr(symb.length*Math.random(),1)}
    return s
}
