from time import sleep
import os
clear = lambda: os.system('cls')
def convert(seconds) -> list:
    seconds = seconds % (24*3600)
    hour = seconds//3600
    seconds %=3600
    minutes = seconds//60
    seconds %=60
    return [hour,minutes,seconds]
def startTimer(sec,cycle,session,right_now):
    clear()
    for x in range(sec):
        rev_time = sec - x
        h,m,s = convert(rev_time)
        print('Cycle : {}'.format(cycle+1))
        print('Session : {}'.format(session+1))
        print('Now : {}'.format(right_now))
        print('Time Remaining :- %.2d : %.2d : %.2d'%(h,m,s))
        sleep(1)  
        clear()   
clear()        
cycles = int(input('Enter the number of cycles\n'))
clear()
sessions = int(input('Enter the number of Pomodoro sessions\n'))
clear()
while True :
    clear() 
    pomodoro_time = int(input('Choose pomodoro time\n10 minutes\n20 minutes\n40 minutes\n1 hour\n'))
    if pomodoro_time == 10:
        pomodoro_time= 600
        break
    if pomodoro_time == 20:
        pomodoro_time = 1200
        break
    if pomodoro_time == 1:
        pomodoro_time == 3600
        break
    else :
        print('Error')
        continue
while True :
    clear()
    mini_break_time = int(input('Choose mini break time\n2 minutes\n5 minutes\n10 minutes\n15 minutes\n'))
    if mini_break_time == 2:
        mini_break_time = 120
        break
    if mini_break_time == 5:
        mini_break_time = 300
        break
    if mini_break_time == 10:
        mini_break_time = 600
        break
    if mini_break_time == 15:
        mini_break_time = 900
        break
    else :
        print('Error')
        continue
while True :    
    clear()
    mega_break_time = int(input('Choose mega break time\n30 minutes\n1 hour\n1 hour 30 minutes\n'))
    if mega_break_time == 30:
        mega_break_time = 1800
        break
    if mega_break_time == 1:
        mega_break_time = 3600
        break
    if mega_break_time ==1.5:
        mega_break_time == 5400
        break
    else :
        print('Error')
        continue
for i in range(cycles) :
    print('{}th Session'.format(i+1))
    for j in range(sessions):
        print('{}th Pomodoro Session'.format(j+1))
        startTimer(pomodoro_time,i,j,'Pomodoro')
        print('{}th Pomodoro Session is over'.format(j+1))
        if j+1!=sessions:
            print('Mini break time')
            startTimer(mini_break_time,i,j,'Mini Break')
            print('Mini break over')
        print('{}th Pomodoro Session over'.format(j+1))
    print('{}th Cycle is over'.format(j+1))
    if i+1==cycles:
        print('Cycles over')
        quit()
    startTimer(mega_break_time,i,j,'Mega Break')
    print('{}th Cycle over'.format(i+1))
