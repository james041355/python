# 引用必要套件  這是測試環境(pythontest) 不是帳務所在地 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np





# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('/pythontest-64730-firebase-adminsdk-kywz2-4580bb3d0d.json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred,{
	'databaseURL':'https://pythontest-64730-default-rtdb.firebaseio.com'})


def readdate(dateset):#讀取
    ref=db.reference(dateset)
                     
    return(ref.get())

def update(dateset,datenames,date):##建立 位置/檔名(標籤)/資料/
    ref=db.reference(dateset)
    ref.update({datenames:date})

def deldate(dateset):#刪除位置 位置/檔名(標籤)
    ref=db.reference(dateset)
    ref.set({})

def show_goods(Atemp,change,path,lable):
    print()
    path=path
    lable=lable

    change=change
    Atemp=Atemp
    if change==0:
        for i in range(len(Atemp)):
            if i==1:
                print(list1[i],"-----",Atemp[i],"______",
                      "加稅價","-----","{:.2f}".format(Atemp[i]*1.05))
            else:
                print(list1[i],"-----",Atemp[i])
    else:
        for i in range(len(Atemp)):
            if i==1:
                print(list1[i],"-----",Atemp[i],"______",
                      "加稅價","-----","{:.2f}".format(Atemp[i]*1.05))
            else:
                print(list1[i],"-----",Atemp[i])
        print("\n需要修改  1: 要修改 2 :不須修改")
        number=int(input())
        if number==1:
            for i in range(len(Atemp)):
                if i==1:
                    print(i+1,":",list1[i],"-----",Atemp[i],"______",
                          "加稅價","-----","{:.2f}".format(Atemp[i]*1.05))
                else:
                    print(i+1,":",list1[i],"-----",Atemp[i])
            print("\n需要修改的選項  選 9 : 結束")
            number=int(input())
            if number==9:

                show_goods(Atemp,0,path,lable)
            else:    
                print(list1[number-1],"-----","(",Atemp[number-1],")  ",end="")
                Atemp[number-1]=input()
                print()
                show_goods(Atemp,1,path,lable)
        else:                        
            show_goods(Atemp,0,path,lable)
            update(path,lable,Atemp)

temp=["平板",3.8,5,10,"k21","片",10,102]
temp1=["二連平板",8,10,20,"k22","片",10,102]
temp2=["4143單管",220,250,350,"w4143","組",10,102]
Atemp=[]
total=0



#update('/temp','k21',temp)
#update('/temp','k22',temp1)
#update('/temp','w4143',temp2)

#Atemp=readdate('temp/k21')
path="temp/"
lable="k22"
Atemp=readdate(path+lable)


list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]

list2= Atemp
col1 = "貨品欄"
col2 = "產品資訊"
#data = pd.DataFrame({col1:list1,col2:list2})

#data.to_excel('/Users/home/Desktop/test2.xlsx', sheet_name='sheet1', index=False)


show_goods(Atemp,1,path,lable)  


















wire={'x02c2':['2平方二芯電纜線',1089,1],
      'x02c3':['2平方三芯電纜線',1425,1],
      'x35c2':['3.5平方二芯電纜線',1520,1],
      'x35c3':['3.5平方三芯電纜線',2079,2],
      'x55c2':['5.5平方二芯電纜線',2235,2],
      'x55c3':['5.5平方三芯電纜線',3076,2],
      'x08c2':['8平方二芯電纜線',3106,2],
      'x08c3':['8平方三芯電纜線',4313,2],
      'x14c3':['14平方三芯電纜線',7436,3],
      'x16c2':['1.6二芯白扁線',700,3],
      'x20c2':['2.0二芯白扁線',1000,3],
      'x16':['1.6單芯電線',232,4],
      'x20':['2.0單芯電線',350,4],
      'x35':['3.5單芯電線',459,4],
      'x55':['5.5單芯電線',708,4],
      'x08':[' 8單芯電線',1009,4]
      }

#test2=wire.get('x02c2')
#print(test2[0])
#update('/temp','use2',wire)  
