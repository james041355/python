A=[0,0,0,0] 
B=[0,0,0,0]
import random



A[0]=random.randrange(10)

A[1]=random.randrange(10)
while A[0] ==  A[1]:
    A[1]=random.randrange(10)

A[2]=random.randrange(10)
while A[0] ==  A[2] or A[1] == A[2]:
    A[2]=random.randrange(10)
A[3]=random.randrange(10)
while A[0] ==  A[3] or A[1] == A[3] or A[2] == A[3]:
    A[3]=random.randrange(10)
#答案print("a ia ",A)



pointa=0
pointb=0
correct=0

while correct != 1:
    print("輸入四位數數字")
    guess=int (input())
    while guess//1000 ==0 or guess//1000>=10:
        print("輸入四位數數字")
        guess=int (input())
        
    k=1000
    keep=guess
    for i in range(4):
        B[i]=int(guess//k)
        guess=guess % k
        k=k/10

    for i in range(4):
        for j in range(4):
            if A[i]==B[j]:
                if i==j:
                    pointa=pointa+1
                else:
                    pointb=pointb+1
    print("你猜的數字 ",keep,"結果是 ",pointa," A",pointb," B")                
    if pointa==4:
        correct=1
        
    pointa=0
    pointb=0   
    










