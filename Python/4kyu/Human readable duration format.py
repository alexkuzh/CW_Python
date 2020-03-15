# https://www.codewars.com/kata/52742f58faf5485cae000b9a
def format_duration(seconds):
    if seconds == 0: return 'now'
    a = [[seconds // (3600 * 24 * 365), 'year', 'years'], [seconds // (3600 * 24) % 365, 'day', 'days'],
         [seconds // (3600) % 24, 'hour', 'hours'], [seconds // (60) % 60, 'minute', 'minutes'],
         [seconds % 60, 'second', 'seconds']]
    s = ', '.join([str(x[0]) + ' ' + x[1] if x[0] == 1 else str(x[0]) + ' ' + x[2] for x in a if x[0] > 0])
    try:
        return s[:s.rindex(',')] + ' and' + s[s.rindex(',') + 1:]
    except:
        return s
