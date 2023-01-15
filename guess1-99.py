
import random
number=random.randrange(100)
first=1
end=99
#答案print (number)
correct=0
times=1
print("猜數字範圍",first,"~~~",end)
while(correct != 1):
   
    guess=int(input("輸入一數字   ")) 
    if(guess > number):
              end=guess  
              print("猜數字範圍",first,"~~~",end)
              times=times+1
              
    elif(guess == number):
              print ("答對了 答案是",guess,"你猜了",times," 次")
              correct=1
    else:
              first=guess
              print("猜數字範圍",first,"~~~",end)
        
              times=times+1
