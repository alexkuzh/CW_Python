# n : number of intervals
def len_curve(n):
    h = 1/n
    coordinates = []
    for i in range(n+1):
        x = i*h
        y = x*x
        coordinates.append((x, y))
    arc = 0
    for i in range(n):
        dx = coordinates[i][0] - coordinates[i+1][0]
        dy = coordinates[i][1] - coordinates[i+1][1]
        arc += (dx*dx + dy*dy)**0.5
    return round(arc,9)