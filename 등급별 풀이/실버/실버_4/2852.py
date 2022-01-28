def time_to_second(timer):
    M, S = map(int, timer.split(':'))
    return M*60 + S

def second_to_time(second):
    print('%s:%s' %(str(second//60).rjust(2, '0'), str(second%60).rjust(2, '0')))

n = int(input())
scores = [input().split() for _ in range(n)]
scores.sort(key=lambda x:x[1])
    
team1, team2 = 0, 0
win1_time, win2_time = 0, 0
winner = 0
now = 0

for getter, timer in scores:
    s = time_to_second(timer)
    if getter == '1':
        team1 += 1
    else:
        team2 += 1
        
    if winner == 0 and team1 > team2:
        winner = 1
        now = s
    elif winner == 0 and team2 > team1:
        winner = 2
        now = s
    elif winner == 1 and team1 == team2:
        winner = 0
        win1_time += s - now
    elif winner == 2 and team1 == team2:
        winner = 0
        win2_time += s - now

finish_time = time_to_second('48:00')
if winner == 1:
    win1_time += finish_time-now
elif winner == 2:
    win2_time += finish_time-now

second_to_time(win1_time)
second_to_time(win2_time)

# def time_to_second(MM, SS):
#     return MM*60 + SS

# def second_to_time(s):
#     print('%s:%s' %(str(s//60).rjust(2, '0'), str(s%60).rjust(2, '0')))

# team1, team2 = 0, 0
# win_team1, win_team2 = 0, 0
# now = 0
# finish_time = time_to_second(48, 00)

# for _ in range(int(input())):
#     team, time = input().split()
#     MM, SS = map(int, time.split(':'))
#     seconds = time_to_second(MM, SS)
#     if team1 > team2:
#         win_team1 += (seconds-now)
#     elif team2 > team1:
#         win_team2 += (seconds-now)
        
#     now = seconds
    
#     if team == '1': team1 += 1
#     else: team2 += 1
    
# if team1 > team2:
#     win_team1 += (finish_time-now)
# elif team2 > team1:
#     win_team2 += (finish_time-now)
    
# second_to_time(win_team1)
# second_to_time(win_team2)