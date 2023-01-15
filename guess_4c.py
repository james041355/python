
def show(index):
    for i in range(len(index)):
        print(index[i],sep="  ",end="  ")
            
def test(guessa,array):
    correct=0
    for i in range(len(array)):
         if guessa==array[i-1]:
             print("  你出的牌是  ",guessa)
             correct=1
             print(correct)
             return correct
             break
             
    

A=[1,2,3,4,5,6,7,8,9,10] 
B=[1,2,3,4,5,6,7,8,9,10]
count=10
correct=0
h=0
g=0

import winsound
import random
while count != 0:
    a=random.randrange(count)
    #print(a)
    home=A[a]
    #print("電腦的牌是 ",home)
    del A[a]
    show(B)


    while correct != 1:
        print(" 請出一張牌")
        guess=int(input())
        for i in range(len(B)):
            if guess==B[i-1]:
                #print("你出的牌是  ",guess)
                correct=1
                frequency = 1000
                duration = 1000
                winsound.Beep(frequency, duration)
                del B[i-1]    
         
    if home > guess:
        h=h+1
        print("電腦出牌是 ",home,"你出牌是 ",guess,"你輸了","比分是",h,"---",g)
        correct=0
    elif home < guess:
        g=g+1
        print("電腦出牌是 ",home,"你出牌是 ",guess,"你贏了","比分是",h,"---",g)
        correct=0
    else:
        h=h+1
        g=g+1
        print("電腦出牌是 ",home,"你出牌是 ",guess,"雙方平手","比分是",h,"---",g)
        correct=0
    count=count-1



if h > g:
    print("電腦贏")
elif h < g:
    print(" 你贏了")
else :
    print(" 雙方平手")









