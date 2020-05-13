// https://www.codewars.com/kata/59eb1e4a0863c7ff7e000008/train/python
function getCombinations(space) {
    const result = [];

    for (let i = 0; i < space; ++i) {
        const leftSpace = i;
        const rightSpace = space - i - 1;
        const leftCombinations = leftSpace > 0 ? getCombinations(leftSpace) : [''];
        const rightCombinations = rightSpace > 0 ? getCombinations(rightSpace) : [''];
        for (const left of leftCombinations) {
            for (const right of rightCombinations) {
                result.push(`(${left})${right}`);
            }
        }
    }

    return result;
}


//console.log(getCombinations(1));
//console.log(getCombinations(2));
console.log(getCombinations(3));
//console.log(getCombinations(4));
//console.log(getCombinations(5));
