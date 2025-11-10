def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}
    h = 0
    m = 0
    s = 0
    h += int(seconds/3600)
    m += int((seconds%3600)/60)
    s = seconds - h*3600 - m*60
    
    return {3600: h, 60: m, 1: s}
