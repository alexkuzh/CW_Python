# https://www.codewars.com/kata/5f25f475420f1b002412bb1f/train/python

#letters: abcdefghijklmnopqrstuvwxyz

def find_the_number_plate(customer_id):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    b = customer_id // 999
    return letters[b%26] + letters[(b//26) % 26] + letters[(b // 676) % 26] + str(customer_id % 999+1).zfill(3)


print(find_the_number_plate(1487))
