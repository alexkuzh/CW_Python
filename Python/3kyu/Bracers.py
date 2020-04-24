def getCombinations(space):
    result = []
    for i in range(0,space):
        leftSpace = i
        rightSpace = space - i - 1
        if leftSpace > 0:
            leftCombinations = getCombinations(leftSpace)
        else:
            leftCombinations = ['*']
        if rightSpace > 0:
            rightCombinations = getCombinations(rightSpace)
        else:
            rightCombinations = ['*']
        for left in leftCombinations:
            for right in rightCombinations:
                result.append('('+left+')'+right)
    return result

print(getCombinations(3))