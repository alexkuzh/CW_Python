# https://www.codewars.com/kata/586a1af1c66d18ad81000134/train/python
def driver(data):
# Start driving here!
    month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    return "{:9<5}".format(data[2].upper())[:5] + data[3][-2] + \
           (str((month.index(data[3][3:6]) + 1)).zfill(2) if data[4] == 'M' else str(month.index(data[3][3:6]) + 51)) + \
            data[3][:2] + data[3][-1] + data[0][0] + (data[1][0] if data[1] != '' else '9') + '9AA'

print(driver(["John", "James", "Lee", "01-Jan-2000", "M"]))