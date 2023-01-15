# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json

import tkinter as tk



# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('/Users/home/Desktop/python/outdata-6457c-firebase-adminsdk-2miud-7b496d14a7 (1).json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred,{
	'databaseURL':'https://outdata-6457c.firebaseio.com'})


def readdate(dateset):#讀取
    ref=db.reference(dateset)
    #print(ref.get())                 
    return(ref.get())

def update(dateset,datenames,date):##建立 位置/檔名/資料/
    ref=db.reference(dateset)
    ref.update({datenames:date})

def deldate(dateset):#刪除位置
    ref=db.reference(dateset)
    ref.set({})

def show_goods(Atemp):
    for i in range(len(Atemp)):
        if i==1:
            print(list1[i],"-----",Atemp[i]
                  ,"______","加稅價","-----","{:.2f}".format(float(Atemp[i])*1.05))
        else:
            print(list1[i],"-----",Atemp[i])

def firebase_get(a):
    date_temp = json.loads(readdate(a))
    #print(date_temp)
    return(date_temp)

def show_number(a):
    print()
    for i in range(2,goods_a):
        d1=date_temp.get(str(i))
        d2=json.loads(d1)
        if(a==d2[4]):
            show_goods(d2)
            correct=1   

#IN_temp=readdate('tbuiness/6')

#IN_temp = json.loads(readdate('tbuiness/7'))#將jason轉成array
#str1 = json.dumps(j)#dict包含list轉JSON字串


#show_goods(IN_temp)

#for hh in date_temp:#拿到字典的key {key,value}
#goods_a=int(readdate('tbuiness/a'))
#print (goods_a)

date_temp=[]
test2='tbuiness/'
date_temp=(readdate(test2))#產品與電線用

print(" 1 :產品查詢\n","2 :電線查詢\n")
choose=int(input())


if(choose==1):
    total=0
    IN_tempp=[]
    list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]
    test2=[]
    
    
    goods_a= int(date_temp.get('a'))#產品數量
    correct=0          
    list_inquire=[]
    number=input("產品查詢名稱或編號 :   ")
    for i in range(2,goods_a):
        if(correct!=1):
            d1=date_temp.get(str(i))
            d2=json.loads(d1)
            if(number in d2[0] or number in d2[4] ):
            #list_inquire.append(i)
                list_inquire.append(d2)
                correct=0

    if(len(list_inquire)==0):
        print("找不到資料")   
    elif(len(list_inquire)==1):
        print(number) 
        show_number(number)
    else:
        for i in range(len(list_inquire)):
            print(i+1,"  ",list_inquire[i-1][0],"(",list_inquire[i-1][4],")")

    
        number=int(input("選項號碼   :"))

        while(number > len(list_inquire)):
            number=int(input("選項號碼   :"))

        show_number(list_inquire[number-2][4])    

        print('end')
if(choose==2):
    

    window = tk.Tk()
    window.title('GUI')
    window.geometry('380x400')
    window.resizable(False, False)
    window.iconbitmap('icon.ico')
    window.mainloop()
    test = tk.Button(text="測試")
    test.pack(side="top")       




   



       
