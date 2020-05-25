//https://www.codewars.com/kata/57a429e253ba3381850000fb/train/javascript
function bmi(weight, height) {
    let bmi = weight / (height ** 2)
    if (bmi > 30) {return "Obese"}
    if (bmi <= 18.5){ return "Underweight"}
    if (bmi <= 25.0) {return "Normal"}
    if (bmi <= 30.0) {return "Overweight"}
}