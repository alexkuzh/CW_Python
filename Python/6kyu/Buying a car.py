# https://www.codewars.com/kata/554a44516729e4d80b000012/train/python
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # your code
    month = 0
    if startPriceOld - startPriceNew >=0:
        return [month, int(startPriceOld - startPriceNew)]
    price = (1 - percentLossByMonth / 100) * (startPriceOld - startPriceNew) + savingperMonth
    while price < 0:
        month += 1
        price = (1 - percentLossByMonth / 100) * (startPriceOld - startPriceNew) + savingperMonth*month
        # print(f' in month {(month, int(price), percentLossByMonth, startPriceOld, startPriceNew , savingperMonth*month)}')
        if price > 0:
            return [month, round(price)]
        startPriceOld = (1 - percentLossByMonth / 100) * startPriceOld
        startPriceNew = (1 - percentLossByMonth / 100) * startPriceNew
        percentLossByMonth = percentLossByMonth + (0.5 if month % 2 else 0)
    return [month, round(price)]


print(nbMonths(2312, 12312, 1000, 1.5))
