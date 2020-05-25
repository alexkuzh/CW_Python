// https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/javascript
function evaporator(content, evap_per_day, threshold){
    d = 0
    content = 100
    while (content>threshold){
        d +=1
        content = content * (1-evap_per_day/100)
    }
    return d
}


console.log(evaporator(10,10,10))