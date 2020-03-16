// https://www.codewars.com/kata/573023c81add650b84000429
function countGrade(scores){
    //coding here...
    let a = {}
    a['S'] = scores.filter(x=>x==100).length
    a['A'] = scores.filter(x=>x<100&&x>=90).length
    a['B'] = scores.filter(x=>x<90&&x>=80).length
    a['C'] = scores.filter(x=>x<80&&x>=60).length
    a['D'] = scores.filter(x=>x<60&&x>=0).length
    a['X'] = scores.filter(x=>x==-1).length
    return a
}
