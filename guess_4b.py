
def show(index):
    for i in range(len(index)):
        if  index[i][0] != 0 :
            print("數字 ",index[i][0],"是",index[i][1]," A",index[i][2]," B")
            



A=[0,0,0,0] 
B=[0,0,0,0]
C=[[0]*3 for i in range(10)]
D=[]
import random



A[0]=random.randrange(10)
while A[0]==0:
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
##print("a ia ",A)


point=0
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
    
  
    
    C[point][0]=keep
    C[point][1]=pointa
    C[point][2]=pointb
    point=point+1
    
    
    show(C)
    

    if pointa==4:
        correct=1
    del D[:]    
    pointa=0
    pointb=0   
    










