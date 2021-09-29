# https://www.hackerrank.com/challenges/the-time-in-words/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def timeInWords(h, m):
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
               11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    h1 = 1 if h == 12 else h+1
    minut = 'minute' if m ==1 else 'minutes'
    if m == 0:
        return f"{numbers[h]} o' clock"
    if m == 15:
        return f"quarter past {numbers[h]}"
    if m == 30:
        return f"half past {numbers[h]}"
    if m == 45:
        return f"quarter to {numbers[h1]}"
    if m < 30:
        if m >= 20:
            return f"twenty {numbers[m-20]} {minut} past {numbers[h]}"
        else:
            return f"{numbers[m]} {minut} past {numbers[h]}"
    if m > 30:
        if m < 40:
            return f"twenty {numbers[40-m]} {minut} to {numbers[h1]}"
        else:
            return f"{numbers[60-m]} {minut} to {numbers[h1]}"


print(timeInWords(1, 1))
