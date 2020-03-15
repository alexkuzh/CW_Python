# https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds):
    # Do something
    return '{hh}:{mm}:{ss}'.format(hh=str(seconds // 3600).zfill(2), mm=str((seconds // 60) % 60).zfill(2),
                                   ss=str(seconds % 60).zfill(2))
