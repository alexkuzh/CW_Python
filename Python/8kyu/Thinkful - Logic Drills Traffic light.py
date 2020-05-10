# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python
def update_light(current):
    # Your code here.
    if current == 'green': return 'yellow'
    if current == 'yellow': return 'red'
    if current == 'red': return 'green'

#    return {"green": "yellow", "yellow": "red", "red": "green"}[current]