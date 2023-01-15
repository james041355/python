# 引用必要套件
import firebase_admin
from firebase_admin import credentials


#from firebase_admin import firestore
from firebase_admin import db
#import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
import json
import datetime
from datetime import date
import tkinter as tk

# 引入訊息視窗模組
import tkinter.messagebox

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('/Users/home/Desktop/python/outdata-6457c-firebase-adminsdk-2miud-7b496d14a7 (1).json')

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred,{
	'databaseURL':'https://outdata-6457c.firebaseio.com'})





def show_allform_window():#日期,序號,廠商名,資料
    
    window = tk.Tk()

    window.title('輸入表單')#程式上方的文字
    window.geometry("1300x700+25+25")
    window.resizable(False, False)#定義可不可以被使用者放大縮小視窗
    
    
    def check_goods(number,flag):#有相同產品名稱或相同編號####
    
        for i in range(2,goods_a+1):
            d1=date_temp.get(str(i))
            d2=json.loads(d1)
            if(number == d2[0] or number == d2[4] ):
                test_show_1("有相同產品名稱或相同編號")
                #print(list1[0],"  :",end='')
                #number=input()
                flag =1
                print(i)
                break
        return flag

    def left_calean():#清除左邊顯示
        Canvas=tk.Canvas
        cv = Canvas(window,width=250, height=250)#,bg = 'white'
            #           创建一个矩形，坐标为(10,10,110,110)
            #cv.create_rectangle(10,10,110,110)
        cv.place(x=0,y=250)

    def middle_clean():#清除中間顯示
        Canvas=tk.Canvas
        cv = Canvas(window,width=350, height=600)#,bg = 'white'
            #           创建一个矩形，坐标为(10,10,110,110)
            #cv.create_rectangle(10,10,110,110)
        cv.place(x=300,y=0)

    def right_clean():#清除右邊顯示
        Canvas=tk.Canvas
        cv = Canvas(window,width=600, height=700)#,bg = 'white'
            #           创建一个矩形，坐标为(10,10,110,110)
            #cv.create_rectangle(10,10,110,110)
        cv.place(x=650,y=0)
    
    #0011   #p002
    def find_goods(keyin,flag):#找到 產品  資料  不顯示
        list_inquire=[] #收集找到的值
        for i in range(2,goods_a+1):
            d1=date_temp.get(str(i))
            d2=json.loads(d1)
            if(keyin in d2[0] or keyin in d2[4] ):
                list_inquire.append(d2)    
                        
                        

                #print(list_inquire)
        if(len(list_inquire)==0):
            print("找不到資料")   
            test_show_1("找不到資料")
            
        elif(len(list_inquire)==1):
            
            
            find_goods_lable(list_inquire[0][4],flag)
            #01-01-01
        elif(len(list_inquire)>25): 
            test_show_1("請縮小尋找範圍")         
        else:
            #print('@@@@end')
            #test_show_1(len(list_inquire))
            dict_goods={}
            for i in range(len(list_inquire)):
                dict_goods[i]=(list_inquire[i][0],list_inquire[i][4])
            middle_clean()
            middle_show_b(1,"產品資訊",dict_goods,flag)#01-01-02 #p005
    
    #0012  #p003
    def find_goods_lable(keyin,flag):#找到 產品標籤 資料  再顯示
        
        list_inquire=[] #收集找到的值
        
        for i in range(2,goods_a+1):
            d1=date_temp.get(str(i))
            d2=json.loads(d1)
            if(keyin == d2[4] ):
                list_inquire.append(d2)  
                lable= i
                break
        
        middle_clean()
        #test_show_1(lable)#fixfixfxi
        if flag==1:#01-01
            middle_show_a(1,"產品資訊",list_inquire[0],flag)
        if flag==4:
            
            middle_show_a(2,"產品資訊",list_inquire[0],flag)#01-04
        if flag==2:#01-02
            #test_show_1("flag")
            middle_show_b(2,"修改產品資料",list_inquire[0],flag)

        left_calean()
        
    #0013
    def find_goods_lableonly(keyin):#找到 產品標籤
        
        #list_inquire=[] #收集找到的值
        
        for i in range(2,goods_a+1):
            d1=date_temp.get(str(i))
            d2=json.loads(d1)
            if(keyin == d2[4] ):
                #list_inquire.append(d2)  
                lable= i
                break
        
        return lable


    #0010 1 只顯示不修改  2 修改 #01-01 #01-02 #p001
    def keyin_entry(mode,title,flag):# 模式   標頭名稱
        def onok():
                if entry1.get()!= "":
                    #print(entry1.get())
                    #test_show_1(entry1.get())
                    
                    find_goods(entry1.get(),flag)
                    

        left_calean()
        

        if mode==1:#只顯示不修改
            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=20,font = ('Arial', 16))
            title.place(x=0,y=250)
            entry1 = tk.Entry(window, width = 20,bd=5,font = ('Arial', 16))    # 輸入欄位所在視窗  # 輸入欄位的寬度                    
            entry1.place(x=0,y=280)
            button = tk.Button(window, text="ok" ,fg="#8B008B", bg="#7AFEC6", width=10,font = ('Arial', 16),
            command=onok)
            button.place(x=60,y=310)

        else:
            #left_calean()
            print("enf")

    
    

    def update(dateset,datenames,date):##建立 位置/標籤/資料/
        ref=db.reference(dateset)
        ref.update({datenames:date})

    def deldate(dateset):#刪除位置(位置+標籤)
        ref=db.reference(dateset)
        ref.set({})
    
    
    
    
    
    ####0001
    def left_show(mode,title,temp):#模式 0 不顯 1 顯示,表頭,資料
        #print("left show=",date_temp.get("a"))
        mode=mode
        title=title
        temp=temp
        #main_read()
        #left_calean()
        middle_clean()
        #date_temp=(readdate(path_goods))#產品與電線用
        if mode==1:
            left_start_x=10
            left_start_y=10
            
            def Selection ():
                
                keep_temp.append(var.get())
                print(keep_temp)
                test_show_1(keep_temp)
                if keep_temp[0] != 88:
                    
                    if keep_temp[0]==1:
                        left_show(1,"產品查詢",A1)
                        #print(len(keep_temp))
                        if len(keep_temp)>=2:
                            if  keep_temp[1]==3:#有後續動作
                                #left_show(1,"SAVE",A11)###########
                                #keyin_entry(1,"產品名稱",2)
                                temp=["",0,0,0,"","",0,""] #01-03use #p011
                                middle_show_b(3,"建立新產品",temp,3)
                                if keep_temp[2]>65:
                                    keep_temp.pop()
                                    keep_temp.pop()
                                    left_show(1,"產品查詢",A1)
                            
                            elif keep_temp[1]==4: #01-04
                                keep_temp.pop()
                                left_show(1,"刪除產品",A1)
                                keyin_entry(1,"刪除產品名稱",4)#####1-???
                            
                            elif keep_temp[1]>=4:
                                keep_temp.pop()
                                keep_temp.pop()#回主畫面
                                left_show(1,"主畫面",tops)
                            
                            elif  keep_temp[1]==2 :#01-02
                                keep_temp.pop()
                                left_show(1,"修改產品",A1)
                                keyin_entry(1,"修改產品名稱",2)#####1-2???
                            
                            else:
                                #無  後續動作 
                                keep_temp.pop()
                                left_calean()
                                middle_clean()
                                keyin_entry(1,"產品名稱",1)#01-00
                                left_show(1,"產品查詢",A1)

                    elif keep_temp[0]==2:
                        left_show(1,"電線查詢",B1)
                        if len(keep_temp)>=2:
                            if keep_temp[1]==2 :#有後續動作
                                left_show(1,"SAVE / DELETE ",B11)
                                if keep_temp[2]>65:
                                    keep_temp.pop()
                                    keep_temp.pop()
                                    left_show(1,"電線查詢",B1)
                            
                            
                            elif keep_temp[1]>=4:
                                keep_temp.pop()
                                keep_temp.pop()#回主畫面
                                left_show(1,"主畫面",tops)
                            
                            else:
                                #無  後續動作 
                                keep_temp.pop()
                                left_show(1,"電線查詢",B1)#02-01
                                dict_goods={}
                                for i in range(len(wire_a)): 
                                    dict_goods[i]=wire_a[i]
                                print(len(wire_a))
                                middle_show(2,"line use",dict_goods,2)
                                #test_show_1(wire_a[0])
                    
                    elif keep_temp[0]==4:
                        left_show(1,"貨物進出查詢",D1)
                        if len(keep_temp)>=2:
                            if  keep_temp[1]>=4:
                                keep_temp.pop()
                                keep_temp.pop()#回主畫面
                                left_show(1,"主畫面",tops)
                            
                            else:
                                #無  後續動作 
                                keep_temp.pop()
                                left_show(1,"貨物進出查詢",D1)
                    elif keep_temp[0]==5:
                        left_show(1,"廠商/客戶 設定",E1)
                        if len(keep_temp)>=2:
                            if  keep_temp[1]>=4:
                                keep_temp.pop()
                                keep_temp.pop()#回主畫面
                                left_show(1,"主畫面",tops)
                            
                            else:
                                #無  後續動作 
                                keep_temp.pop()
                                left_show(1,"廠商/客戶 設定",E1)
                    else:
                        
                        left_show(1,"表單查詢",C1)
                        #print(len(keep_temp))
                        if len(keep_temp)>=2:
                            if keep_temp[1]>65:
                                #keep_temp.pop()
                                keep_temp.pop()
                                keep_temp.pop()#回主畫面
                                left_show(1,"主畫面",tops)
                            
                            if keep_temp[1]==2 :#有後續動作
                                left_show(1,"增加 /刪除 表單",C11)
                                if  keep_temp[2]>65:
                                    keep_temp.pop()
                                    keep_temp.pop()
                                    keep_temp.pop()#回主畫面
                                    left_show(1,"主畫面",tops)
                            
                                elif keep_temp[2]==2: #有後續動作
                                    left_show(1,"修改 /刪除 表單",C12)
                                    if keep_temp[3]>65:
                                        keep_temp.pop()
                                        keep_temp.pop()
                                        keep_temp.pop()
                                        keep_temp.pop()
                                        left_show(1,"主畫面",tops)
                                    elif keep_temp[3]==2:
                                        left_show(1,"刪除選項",A12)
                                        if keep_temp[4]>65:
                                            keep_temp.pop()
                                            keep_temp.pop()
                                            keep_temp.pop()
                                            keep_temp.pop()
                                            keep_temp.pop()
                                            left_show(1,"主畫面",tops)
                                    else:
                                        keep_temp.pop()
                                        left_show(1,"修改 /刪除 表單",C12)
                                else:

                                #無  後續動作 
                                    keep_temp.pop()
                                    left_show(1,"增加 /刪除 表單",C11)
                            
                            else:

                                #無  後續動作 
                                keep_temp.pop()
                                left_show(1,"表單查詢",C1)    
                            
                            

                else:
                    ###test_temp.append(66)
                    window.destroy()#關閉螢幕 break break 
                    #test_show_2("end  end")
                    print("test_",test_temp)

    
            var = tk.IntVar()#設置 var 內容
            var.set(0)
            
            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=30,font = ('Arial', 11))
            title.place(x=left_start_x,y=left_start_y)
            left_start_y=left_start_y+30

            for val, top in temp.items():
                R=tk.Radiobutton (window,text=top,indicatoron=0,variable=var, value=val,
                command=Selection,bg='yellow',width=30,font = ('Arial', 11))
                R.place(x=left_start_x,y=left_start_y)
                left_start_y=left_start_y+30
            #test_show_1(keep_temp)
            

    def test_show_1(temp):###測試顯示用
        title = tk.Label(window, text=temp ,fg="#8B008B", bg="#7AFEC6", width=30)
        title.place(x=0,y=600)###測試顯示用
    def test_show_2(temp):###測試顯示用
        title = tk.Label(window, text=temp ,fg="#8B008B", bg="#7AFEC6", width=30)
        title.place(x=0,y=650)###測試顯示用
    #0014
    def data_save_or_delete(mode,temp):#01-02-04 #p009
        
        if mode==1:
            lable=find_goods_lableonly(temp[4])
            temp=json.dumps(temp)    
            print(temp)
            print(lable)#01-02
            update(path_goods,lable,temp)##建立 位置/檔名/資料/    
            test_temp.append(66)
            window.destroy()#關閉螢幕 
        elif mode==2:#p012
            correct=0
            if temp[0] ==" " or temp [4]== "" or temp [5]== "":
                correct=1
            if temp[1] ==0 or temp [2]== 0  or temp [3]== 0 or temp [6]== 0:
                correct=1
            
            if correct ==1 :
                test_show_1("產品資料不完整")
            else:
                test_show_1("準備純黨")
                print(temp)
                print(path_goods)
                print(goods_a+1)#nownow
                print(goods_a)
                temp=json.dumps(temp)
                update(path_goods,goods_a+1,temp)##建立 位置/檔名/資料/    
                update(path_goods,'a',goods_a+1)
                
                test_temp.append(66)
                window.destroy()#關閉螢幕
                
            
    #0014
    def ask_yes_or_no(mode,temp):#01-04-04               
        lable=find_goods_lableonly(temp[4])
        #print("ttt==",lable)
        
        def sure():
            #print(lable)
            #print("old=",date_temp.get("a"))
            
            #print(goods_a)
            if mode==1:#01-04 use 刪除畫面 #change999
                if int(lable)==int(goods_a):
                    
                    deldate(path_goods+str(lable))
                    update(path_goods,'a',goods_a-1)
                    #update(path_goods,'keep',keep_for_net+1)#for test
                    test_show_1("del_date")
                    #main_read()
                
                else:
                        
                    temp=readdate(path_goods+str(goods_a))
                    #print(temp)
                    update(path_goods,lable,temp)
                    #update(path_goods,'keep',keep_for_net+1)#for test
                    deldate(path_goods+str(goods_a))
                    update(path_goods,'a',goods_a-1)
                    test_show_1("del_date")
                    #print("del_date")
                    #main_read()
            
            test_temp.append(66)
            window.destroy()#關閉螢幕 
            
            
        
        def notsure():
            left_show(1,"主畫面",tops)
            left_calean()
            middle_clean()
            
            test_show_1("not delete goods")#01-04-04
        
        
        button = tk.Button(window, text="確定刪除" ,fg="#8B008B", bg="#7AFEC6", width=9,font = ('Arial', 16),
        command=sure)
        button.place(x=300,y=310)
        button2 = tk.Button(window, text='不刪除' ,fg="#8B008B", bg="#7AFEC6", width=9,font = ('Arial', 16),
        command=notsure)
        button2.place(x=425,y=310)

        




    #0002 顯示選項
    def middle_show(mode,title,temp,flag):#模式 0 不顯 1 只顯示產品,表頭,資料
        list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]
        print("flag==",flag)
        #fix=0

        def keyin_entry1(title,choose,temp):# 模式   標頭名稱  
            #01-02-03
            left_calean()
            def fix():
                
                #test_show_2(entry1.get())
                if entry1.get()!= "" and entry1.get().isdigit()==True:
                    #print(entry1.get())
                    #test_show_1(entry1.get())
                    temp[choose]=entry1.get()
                    
                    middle_show(1,"修改畫面",temp,2)
                    #middle_show_b(1,"修改畫面",temp,2)
                    left_calean()
                    #print(temp)
            
            def save():
                #test_show_1("save")
                #print(temp)
                data_save_or_delete(1,temp)
            

            #left_calean()
            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=20,font = ('Arial', 16))
            title.place(x=0,y=250)
            entry1 = tk.Entry(window, width = 20, text='y',bd=5,font = ('Arial', 16))    # 輸入欄位所在視窗  # 輸入欄位的寬度                    
            entry1.place(x=0,y=280)
            button = tk.Button(window, text="fix" ,fg="#8B008B", bg="#7AFEC6", width=9,font = ('Arial', 16),
            command=fix)
            button.place(x=0,y=310)
            button2 = tk.Button(window, text='save' ,fg="#8B008B", bg="#7AFEC6", width=9,font = ('Arial', 16),
            command=save)
            button2.place(x=125,y=310)


            
            #test_show_1(temp)
        
        
            


        
        if mode==1 :
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=30,font = ('Arial', 14))
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            if flag==1 or flag == 4 :#01-01-03 #01-04-03
                for i in range(len(list1)):
                    R=tk.Label(window, text=list1[i]+":"+str(temp[i]),fg="#8B008B", width=30,font = ('Arial', 13))
                    R.place(x=middle_start_x,y=middle_start_y)
                    middle_start_y=middle_start_y+30
                if flag==4:
                    ask_yes_or_no(temp)#01-04-03
                    #print(temp)
                    #test_show_1(temp)
            elif flag==5:
                #test_show_1("02-01")
                for i in range(len(wire)):
                    R=tk.Label(window, text=wire[i][0],fg="#8B008B", width=30,font = ('Arial', 13))
                    R.place(x=middle_start_x,y=middle_start_y)
                    middle_start_y=middle_start_y+30    
            else:
                dict_goods={} #01-02-03
                for i in range(len(temp)):
                    dict_goods[i]=list1[i]+" : "+str(temp[i])
                #print(dict_goods)
                def Selection ():
                #print(temp [var.get()])
                #print(var.get())
                    #test_show_1(var.get())
                    if(var.get()==1 or var.get()==2 or var.get()==3 or var.get()==6 ):
                        
                        head=list1[var.get()]+str(temp[var.get()])
                        keyin_entry1(head,var.get(),temp)
                    #number=(temp.get(var.get()))
                    #print(number[1])
                    #find_goods_lable(number[1])
                var = tk.IntVar()#設置 var 內容
                var.set(0)

                for val, top in dict_goods.items():
                    R=tk.Radiobutton (window,text=top,indicatoron=0,variable=var, value=val,
                    command=Selection,bg='yellow',width=30,font = ('Arial', 13))
                    R.place(x=middle_start_x,y=middle_start_y)
                    middle_start_y=middle_start_y+30
        
        elif mode==2:
            
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", 
            width=30,font = ('Arial', 13))#,font = ('Arial', 14)
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            
            def Selection ():
                if flag==1:
                    #print(temp [var.get()])
                    #print(var.get())
                    #test_show_1(flag)
                    number=(temp.get(var.get()))
                    #print(number[1])
                    find_goods_lable(number[1],flag)
                else:
                    #test_show_1(flag)#02-01-01
                    wire_use=temp[var.get()]
                    print(temp[var.get()])
                    print(len(wire_use))
                    middle_clean()
                    middle_show(1,"line",wire_use,5)
            var = tk.IntVar()#設置 var 內容
            var.set(0)

            for val, top in temp.items():
                R=tk.Radiobutton (window,text=top,indicatoron=0,variable=var, value=val,
                command=Selection,bg='yellow',width=30,font = ('Arial', 13))
                R.place(x=middle_start_x,y=middle_start_y)
                middle_start_y=middle_start_y+30
        else :
            middle_clean()
    
    
    #0002a 顯示選項 #p004
    def middle_show_a(mode,title,temp,flag):#模式 0 不顯 1 只顯示產品,表頭,資料
        
        
        if mode==1 :#01-01-use
            list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=30,font = ('Arial', 14))
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            
            for i in range(len(list1)):
                R=tk.Label(window, text=list1[i]+":"+str(temp[i]),fg="#8B008B", width=30,font = ('Arial', 13))
                R.place(x=middle_start_x,y=middle_start_y)
                middle_start_y=middle_start_y+30
        
        if mode== 2:#01-04-use #p010 
            list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=30,font = ('Arial', 14))
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            
            for i in range(len(list1)):
                R=tk.Label(window, text=list1[i]+":"+str(temp[i]),fg="#8B008B", width=30,font = ('Arial', 13))
                R.place(x=middle_start_x,y=middle_start_y)
                middle_start_y=middle_start_y+30
            ask_yes_or_no(1,temp)#01-04-03
                    #print(temp)
            #test_show_1(temp)
    
    
    
    
    
    
    #0002b #p005
    def middle_show_b(mode,title,temp,flag):#模式 0 不顯 1 只顯示產品,表頭,資料
        list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]
        

        def keyin_entry1(title,choose,temp):# 模式   標頭名稱 #p007
            #01-02-03

            def fix():
                
                #test_show_2(entry1.get())
                if flag !=3 :
                    if entry1.get()!= "" and entry1.get().isdigit()==True:
                        #print(entry1.get())
                        #test_show_1(entry1.get())
                        temp[choose]=entry1.get()
                        middle_show_b(2,"修改畫面",temp,flag) #p008
                        #middle_show(1,"修改畫面",temp,2)
                        left_calean()
                        #print(temp)
                else:
                    #test_show_1(choose)
                    if choose==0 or choose==4: #P011 # 01-03 USE
                        test=check_goods(entry1.get(),0)
                        if entry1.get()!= "" and test !=1  :
                            if choose==0:#產品名
                                temp[choose]=entry1.get()
                                temp[7]=entry1.get()
                            else:
                                temp[choose]=entry1.get()#產品編號
                            middle_show_b(3,"修改畫面",temp,flag) 
                    elif choose==1 or choose==2 or choose==3 or choose==6:
                        if entry1.get()!= "" and entry1.get().isdigit()==True:
                            temp[choose]=int(entry1.get())#得輸入數字欄位
                            middle_show_b(3,"修改畫面",temp,flag) 
                    else:
                        if entry1.get()!= "":
                            temp[choose]=entry1.get()
                            middle_show_b(3,"修改畫面",temp,flag)
                    left_calean()
                    #test_show_1(choose)
            def save():
                if flag != 3:
                    data_save_or_delete(1,temp)#01-02-04 #p009
                else:
                    data_save_or_delete(2,temp)#01-03 use #p012

            #left_calean()
            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", width=20,font = ('Arial', 16))
            title.place(x=0,y=250)
            entry1 = tk.Entry(window, width = 20, text='y',bd=5,font = ('Arial', 16))    # 輸入欄位所在視窗  # 輸入欄位的寬度                    
            entry1.place(x=0,y=280)
            button = tk.Button(window, text="fix" ,fg="#8B008B", bg="#7AFEC6", width=9,font = ('Arial', 16),
            command=fix)
            button.place(x=0,y=310)
            button2 = tk.Button(window, text='save' ,fg="#8B008B", bg="#7AFEC6", width=9,font = ('Arial', 16),
            command=save)
            button2.place(x=125,y=310)


        if mode==1:#01-01 #p005a
            
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", 
            width=30,font = ('Arial', 13))#,font = ('Arial', 14)
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            
            def Selection ():
                
                    #print(temp [var.get()])
                    #print(var.get())
                    
                    number=(temp.get(var.get()))
                    print(number[1])
                    #test_show_1(flag)#01-01
                    
                    find_goods_lable(number[1],flag)#
                    
                        
                        
                        
                        
                        
                
            var = tk.IntVar()#設置 var 內容
            var.set(0)

            for val, top in temp.items():
                R=tk.Radiobutton (window,text=top,indicatoron=0,variable=var, value=val,
                command=Selection,bg='yellow',width=30,font = ('Arial', 13))
                R.place(x=middle_start_x,y=middle_start_y)
                middle_start_y=middle_start_y+30
        
        elif mode==2:#01-02 #p005b
            #print(temp)
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", 
            width=30,font = ('Arial', 13))#,font = ('Arial', 14)
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            
            dict_goods={} #01-02-03
            for i in range(len(temp)):
                dict_goods[i]=list1[i]+" : "+str(temp[i])
                #print(dict_goods)
            def Selection ():
                #print(temp [var.get()])
                #print(var.get())
                #test_show_1(var.get())
                if(var.get()==1 or var.get()==2 or var.get()==3 or var.get()==6 ):
                        
                    head=list1[var.get()]+str(temp[var.get()])
                    keyin_entry1(head,var.get(),temp)
                    #number=(temp.get(var.get()))
                    #print(number[1])
                    #find_goods_lable(number[1])
            var = tk.IntVar()#設置 var 內容
            var.set(0)

            for val, top in dict_goods.items():
                R=tk.Radiobutton (window,text=top,indicatoron=0,variable=var, value=val,
                command=Selection,bg='yellow',width=30,font = ('Arial', 13))
                R.place(x=middle_start_x,y=middle_start_y)
                middle_start_y=middle_start_y+30
        elif mode==3 : #p011 #01-03 use
            #test_show_1(flag)
            middle_start_x=300
            middle_start_y=10

            title = tk.Label(window, text=title ,fg="#8B008B", bg="#7AFEC6", 
            width=30,font = ('Arial', 13))#,font = ('Arial', 14)
            title.place(x=middle_start_x,y=middle_start_y)
            middle_start_y=middle_start_y+30
            
            dict_goods={} 
            for i in range(len(temp)):
                dict_goods[i]=list1[i]+" : "+str(temp[i])
                #print(dict_goods)
            def Selection ():
                #print(temp [var.get()])#p011
                #print(var.get())
                
                
                        
                head=list1[var.get()]+str(temp[var.get()])
                keyin_entry1(head,var.get(),temp)
                
                
                    
                    #number=(temp.get(var.get()))
                    #print(number[1])
                    #find_goods_lable(number[1])
            var = tk.IntVar()#設置 var 內容
            var.set(0)

            for val, top in dict_goods.items():
                R=tk.Radiobutton (window,text=top,indicatoron=0,variable=var, value=val,
                command=Selection,bg='yellow',width=30,font = ('Arial', 13))
                R.place(x=middle_start_x,y=middle_start_y)
                middle_start_y=middle_start_y+30
                #print("jjjj")
                #middle_clean()           
                
                
                
            
        
        



    #0003
    def right_show(mode,date,serial,guest,temp):#日期,序號,廠商名,資料:
        date=date
        serial=serial
        guest=guest
        temp=temp
        mode=mode
        right_start=650
        if mode==1:
            keep_temp=[]
            

            def onOK():
                window.destroy()#關閉螢幕
            def onnext():
                keep_temp.append(1)
                window.destroy()#關閉螢幕    
            def onfix():
                keep_temp.append(2)
                window.destroy()#關閉螢幕
            def onsave():
                keep_temp.append(3)
                window.destroy()#關閉螢幕
            def onfixsave():
                keep_temp.append(4)
                window.destroy()#關閉螢幕       

            label_date=tk.Label(window, text = '日期  ',font = ('Arial', 14))
            label_date_in=tk.Label(window, text = date,font = ('Arial', 14))
            label_serial=tk.Label(window, text = '序號  ',font = ('Arial', 14))
            label_serial_in=tk.Label(window, text = serial,font = ('Arial', 14))
            label_name=tk.Label(window, text = '店家名字  ',font = ('Arial', 14))
            label_name_in=tk.Label(window, text = guest,font = ('Arial', 14))
            x=right_start
            y=0
            label_date.place(x=x,y=y)
            x=x+50
            label_date_in.place(x=x,y=y)
            x=x+100
            label_serial.place(x=x,y=y)
            x=x+50
            label_serial_in.place(x=x,y=y)
            x=x+150
            label_name.place(x=x,y=y)
            x=x+100
            label_name_in.place(x=x,y=y)

            # 標示文字
            labela = tk.Label(window, text = '產   品   名   稱  ',font = ('Arial', 14))
            labelb = tk.Label(window, text = '數 量  ',font = ('Arial', 14))
            labelc = tk.Label(window, text = '單 位  ',font = ('Arial', 14))
            labeld = tk.Label(window, text = '單 價  ',font = ('Arial', 14))
            labele = tk.Label(window, text = '小 計  ',font = ('Arial', 14))
            labelf = tk.Label(window, text = '備 註  ',font = ('Arial', 14))
            #labela.pack(side='left')
            x=right_start
            y=50
            labela.place(x=x,y=y)#產   品   名   稱
            x=x+250
            labelb.place(x=x,y=y)#數 量
            x=x+70
            labelc.place(x=x,y=y)#單 位
            x=x+70
            labeld.place(x=x,y=y)#單 價
            x=x+70
            labele.place(x=x,y=y)#小 計
            x=x+70
            labelf.place(x=x,y=y)#備 註
            x=right_start
            y=100
            total=0
            for i in range(len(temp)):
                label = tk.Label(window, text = temp[i][0],font = ('Arial', 14))
                label.place(x=x,y=y)
                x=x+250
                label = tk.Label(window, text = temp[i][1],font = ('Arial', 14))
                label.place(x=x,y=y)
                x=x+70
                label = tk.Label(window, text = temp[i][2],font = ('Arial', 14))
                label.place(x=x,y=y)
                x=x+70
                label = tk.Label(window, text = temp[i][3],font = ('Arial', 14))
                label.place(x=x,y=y)
                x=x+70
                label = tk.Label(window, text = temp[i][3],font = ('Arial', 14))
                label.place(x=x,y=y)
                total=total+temp[i][4]
                #total=0
                x=right_start
                y=y+25
            window.update_idletasks()     
            x=right_start
            y=y+25
            label = tk.Label(window, text = "----------------------------------------------------------------------------------------------------------")
            label.place(x=x,y=y)
            x=right_start+480#總計用r
            y=y+25   
            label = tk.Label(window, text = total,font = ('Arial', 14))
            label.place(x=x,y=y)
            
            blank = 30
            idicent = 170
            button_next = tk.Button(window, text = "下一筆資料", command = onnext,bg='yellow')
            
            #button_next.place(x=idicent*0,y=window.winfo_width()-30)
            button_next.place(x=window.winfo_width()-right_start,y=window.winfo_height()-30)
            
            button_fix = tk.Button(window, text = "修改單筆資料", command = onfix,bg='gray')
            button_fix.place(x=window.winfo_width()-right_start+(idicent*1),y=window.winfo_height()-30)
            button_save = tk.Button(window, text = "儲存表單", command = onsave,bg='yellow')
            button_save.place(x=window.winfo_width()-right_start+(idicent*2),y=window.winfo_height()-30)
            button_fix_save = tk.Button(window, text = "修改成本", command = onfixsave,bg='gray')
            button_fix_save.place(x=window.winfo_width()-right_start+(idicent*3),y=window.winfo_height()-30)
            entry = tk.Entry(window, width = 20,bd=5,font = ('Arial', 18))    # 輸入欄位所在視窗  # 輸入欄位的寬度                    
            entry.place(x=0,y=window.winfo_width()-100)
            
            #print("x width==",window.winfo_width())
            #print("y height==",window.winfo_height())
        else:
            right_clean()
    

    
    
    end=1
    if end == 1:
        keep=[]
        keep_temp=[]
        tops={1:"產品查詢 ", 2 :"電線查詢 ", 3:"表單查詢 ",4 :"貨品進出",  5 :"客戶/廠商 設定",88 :"結束程式"}
        A1={1:"產品查詢 ", 2 :"修改產品資料 ", 3:"建立產品資料 ",4 :"刪除產品資料",  88 :"結束產品查詢",66 :""}
        A11={79:"要存檔 ", 80 :"不要存檔 ",66 :"",67 :" ",68:" ",69 :" "}
        A12={79:"確定刪除 ", 80 :"不要刪除 ",66 :"",67 :" ",68:" ",69 :" "}
        B1={1:"查詢電線價錢與列印 ", 2 :"電線設定檔 ", 3:"更改電線成本 ",  88:"結束電線查詢",66 :"",67 :" "}
        B11={79:"建立電線設定檔",80 :"刪除電線設定檔 ",66 :"",67 :" ",68:" ",69 :" "}
        C1={1:"僅供表單查詢 ", 2 :"增加 /刪除表單", 88:"結束表單查詢",66 :"",67 :" ",68:" "}
        C11={1:"增加新表單", 2 :"修改/ 刪除單日表單 ",66 :"",67 :" ",68:" ",69 :" "}
        C12={1:"修改表單", 2 :"刪除單日表單 ",66 :"結束表單查詢",67 :" ",68:" ",69 :" "}
        D1={1:"全品項查詢", 2 :"單一品項查詢 ",  88:"結束貨品進出",66 :"",67 :" ",68:" "}
        E1={1:"編輯 廠商/客戶 資料  ", 2 :"增加 廠商/客戶 資料", 3:"刪除 廠商/客戶 資料 ",88:"結束貨品進出",66 :"",67 :" "}    
        list1 = ["名稱","成本","大賣","小賣","編號","單位","數量","簡稱"]
        wire=[["2平方二芯電纜線",1089,1],
            ['2平方三芯電纜線',1425,1],
            ['3.5平方二芯電纜線',1520,1],
            ['3.5平方三芯電纜線',2079,2],
            ['5.5平方二芯電纜線',2235,2],
            ['5.5平方三芯電纜線',3076,2],
            ['8平方二芯電纜線',3106,2],
            ['8平方三芯電纜線',4313,2],
            ['14平方三芯電纜線',7436,3],
            ['1.6二芯白扁線',700,3],
            ['2.0二芯白扁線',1000,3],
            ['1.6單芯電線',232,4],
            ['2.0單芯電線',350,4],
            ['3.5平方電線',459,4],
            ['5.5平方電線',708,4],
            ['8平方電線',1009,4]]
        date="20221216"
        serial="123456789"
        guest="123456789"
        temp=[["電磁開關MSO-P40(15HP)",1,"個",100,1000],["789456987555",20,"個",15,300]]
        
        keep_temp=[]
        date_temp=[]
        path_goods='tbuiness/'#產品與電線目錄
        date_temp=(readdate(path_goods))#產品與電線用
        print("read read")
        business_b= int(date_temp.get('b'))#客戶數量
        factory_f= int(date_temp.get('f'))#廠商數量
        goods_a= int(date_temp.get('a'))#產品數量
        wire_a= json.loads(date_temp.get('wire'))#產品數量_
        keep_for_net=readdate(path_goods+"keep")
        print("net==",keep_for_net)
        keep_for_program=int(date_temp.get('keep'))#1229use
        print("program==",keep_for_program)
            ####拿到所有廠商客戶名子
        business_list=[]
        for i in range(1001,int(factory_f)+1):
            #print(json.loads(date_temp.get(str(i)))[1])
            business_list.append(json.loads(date_temp.get(str(i)))[1])
        for i in range(1101,int(business_b)+1):
            #print(json.loads(date_temp.get(str(i)))[1])
            business_list.append(json.loads(date_temp.get(str(i)))[1])
            #########放在business_list
        #print(business_list)
        dict_business_list={}
        for i in range(len(business_list)):
            dict_business_list[i]=business_list[i]
        print(goods_a)
        
        customer=[]#拿到所有 客戶名子
        for i in range(1101,int(business_b)+1):
            #print(json.loads(date_temp.get(str(i)))[1])
            customer.append(json.loads(date_temp.get(str(i)))[1])
        #print(customer)
        #right_show(1,date,serial,guest,temp)#日期,序號,廠商名,資料:
        #right_show(0,date,serial,guest,temp)#日期,序號,廠商名,資料:
        left_show(1,"主畫面",tops)
        print("now now test==",test_temp)
        #keyin_entry(1,"test")
        #keyin_entry(0,"test")
        #middle_show(2,"選擇廠商 /客戶",dict_business_list)
        #middle_show(0,"產品資訊",["1234",10,10,10,"k88","各",10,"1234"])
        
        #print("choose==",keep_temp)
        
        #end_temp=[]
    
    
    
    window.mainloop()

def readdate(dateset):#讀取(位置+標籤)####
    ref=db.reference(dateset)
    #print(ref.get())                 
    return(ref.get())


test_temp=[]
date_temp=[]
keep_temp=[]
date_temp=[]
path_goods='tbuiness/'#產品與電線目錄
date_temp=(readdate(path_goods))#產品與電線用

business_b= int(date_temp.get('b'))#客戶數量
factory_f= int(date_temp.get('f'))#廠商數量
goods_a= int(date_temp.get('a'))#產品數量
wire_a= json.loads(date_temp.get('wire'))#產品數量_
keep_for_net=readdate(path_goods+"keep")
show_allform_window()
#print("222=",test_temp[0])
if len(test_temp) != 0:
    while test_temp[0]==66:
        test_temp=[]
        show_allform_window()

