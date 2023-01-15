import tkinter as tk
# 引入訊息視窗模組
import tkinter.messagebox


def show_form_window(date,serial,guest,temp):#日期,序號,廠商名,資料
    date=date
    serial=serial
    guest=guest
    temp=temp
    print(len(temp))
    window = tk.Tk()

    window.title('輸入表單')#程式上方的文字
    window.geometry("600x600+250+50")
    ## 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)

    window.resizable(False, False)#定義可不可以被使用者放大縮小視窗
    #window.iconbitmap('icon.ico')# 設定程式的圖示，可在括弧中放入檔案路徑

    def hello():
        print("Hello, world.")

    def onOK():
        # 取得輸入文字
        #print("Hello, {}.".format(entry.get()))
        window.destroy()#關閉螢幕
        


    # 以預設方式排版標示文字

    label_date=tk.Label(window, text = '日期  ',font = ('Arial', 14))
    label_date_in=tk.Label(window, text = date,font = ('Arial', 14))
    label_serial=tk.Label(window, text = '序號  ',font = ('Arial', 14))
    label_serial_in=tk.Label(window, text = serial,font = ('Arial', 14))
    label_name=tk.Label(window, text = '店家名字  ',font = ('Arial', 14))
    label_name_in=tk.Label(window, text = guest,font = ('Arial', 14))
    x=0
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
    x=0
    y=50
    labela.place(x=x,y=y)
    x=x+200
    labelb.place(x=x,y=y)
    x=x+70
    labelc.place(x=x,y=y)
    x=x+70
    labeld.place(x=x,y=y)
    x=x+70
    labele.place(x=x,y=y)
    x=x+70
    labelf.place(x=x,y=y)
    x=0
    y=100
    total=0
    for i in range(len(temp)):
        label = tk.Label(window, text = temp[i][0],font = ('Arial', 14))
        label.place(x=x,y=y)
        x=x+200
        label = tk.Label(window, text = temp[i][1],font = ('Arial', 14))
        label.place(x=x,y=y)
        x=x+70
        label = tk.Label(window, text = temp[i][2],font = ('Arial', 14))
        label.place(x=x,y=y)
        x=x+70
        label = tk.Label(window, text = temp[i][3],font = ('Arial', 14))
        label.place(x=x,y=y)
        x=x+70
        label = tk.Label(window, text = temp[i][4],font = ('Arial', 14))
        label.place(x=x,y=y)
        total=total+temp[i][4]
        x=0
        y=y+25

    x=0
    y=y+25
    label = tk.Label(window, text = "----------------------------------------------------------------------------------------------------------")
    label.place(x=x,y=y)
    x=480
    y=y+25   
    label = tk.Label(window, text = total,font = ('Arial', 14))
    label.place(x=x,y=y)


    # 輸入欄位
    entry = tk.Entry(window,     # 輸入欄位所在視窗
                     width = 20) # 輸入欄位的寬度
    entry.pack(side='bottom')

    button = tk.Button(window, text = "OK", command = onOK)

    # 以預設方式排版按鈕
    button.pack(side='bottom')



    window.mainloop()

temp=[["123456789",10,"個",100,1000],["789456987555",20,"個",15,300]]




show_form_window('20220413','bn2202041387','協生',temp)#日期,序號,廠商名,資料
print("this is test ")



















