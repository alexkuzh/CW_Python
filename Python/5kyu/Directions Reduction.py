# https://www.codewars.com/kata/550f22f4d758534c1100025a
def dirReduc(arr):
    i = 0
    while i < len(arr) - 1:
        if ((arr[i] == "NORTH" and arr[i + 1] == "SOUTH") or
                (arr[i] == "SOUTH" and arr[i + 1] == "NORTH") or
                (arr[i] == "WEST" and arr[i + 1] == "EAST") or
                (arr[i] == "EAST" and arr[i + 1] == "WEST")):
            arr.pop(i)
            arr.pop(i)
            i = -1
        i += 1
    return arr
