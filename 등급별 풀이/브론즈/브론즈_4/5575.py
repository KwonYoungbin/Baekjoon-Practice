def timeTosecond(h, m, s):
    return h*3600 + m*60 + s

def secondTotime(s):
    print(s//3600, (s%3600)//60, (s%3600)%60)
    
for _ in range(3):
    time = list(map(int, input().split()))
    work_in = timeTosecond(time[0], time[1], time[2])
    work_out = timeTosecond(time[3], time[4], time[5])
    secondTotime(work_out-work_in)