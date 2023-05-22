from datetime import datetime

def calculate_angle(h, m):
    # Calculate the angle made by the hour hand with respect to 12:00
    hour_angle = 0.5 * (60 * h + m)
    # Calculate the angle made by the minute hand with respect to 12:00
    minute_angle = 6 * m
    # Calculate the absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)
    # Return the smaller angle of the two possible angles
    angle = min(angle, 360 - angle)
    return angle

def ange_hour_minute(chas, minuta):
    minute_angle = minuta * 6
    hour_angle = (chas % 12) * 30 + minuta/2
     return max(hour_angle,minute_angle) - min(hour_angle,minute_angle)

t = datetime.now()

print(ange_hour_minute(t.hour, t.minute))
print(calculate_angle(t.hour, t.minute))
