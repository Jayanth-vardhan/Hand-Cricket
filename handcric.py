from random import randint  as r
from random import choice as c
global t
def user_batting(t):
    urun = 0
    while True:
        x = int(input("enter your runs(between 1-6):"))
        c = r(1,6)
        print("computer score:",c,'\n')
        if(x!=c):
            urun+=x
            if(urun >= t and t!=-1):
                print('You Win!')
                return
        else:
            print('OUT!')
            print('your score is',urun)
            if(urun < t-1):
                print('computer wins')
                return
            break
    if(t == -1):
        print("computer's turn\n computer's target is",urun+1 )
        return urun+1
    
def comp_batting(t):
    crun = 0
    while True:
        x = int(input("enter your runs(between 1-6):"))
        c = r(1,6)
        print("computer score:",c,'\n')
        if(x!=c):
            crun+=c
            if(crun >= t and t!=-1):
                print('computer Wins!')
                return
        else:
            print('OUT!')
            print('computer score is',crun)
            if(crun < t-1):
                print('you win')
                return
            break
    if(t == -1):
        print("your turn\n your target is",crun+1 )
        return crun+1

t = 0
i = 0
ch = input('even or odd:')
a = int(input("enter a number:"))
com = r(1,6)
print('computer:',com)
print('total sum:',com+a)
if(ch == 'even' and ((a+com)%2 == 0)):
    i = int(input('you won,batting(1) or bowling(0):'))
    if(i==1):
        t = user_batting(-1)
        comp_batting(t)
    else:
        t = comp_batting(-1)
        user_batting(t)
elif(ch == 'odd' and ((a+com)%2 != 0)):
    i = int(input('you won,batting(1) or bowling(0):'))
    if(i==1):
        t = user_batting(-1)
        comp_batting(t)
    else:
        t = comp_batting(-1)
        user_batting(t)
else:
    l = ['batting','bowling']
    s = c(l)
    print('you lost,computer chose',s)
    if(s == 'batting'):
        t = comp_batting(-1)
        user_batting(t)
        
    else:
        t = user_batting(-1)
        comp_batting(t)
        



    