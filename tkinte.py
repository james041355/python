import tkinter as tk
# 引入訊息視窗模組
import tkinter.messagebox

window = tk.Tk()

window.title('Hello World')#程式上方的文字
window.geometry("300x300+250+150")
## 設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為 (250, 150)

window.resizable(False, False)#定義可不可以被使用者放大縮小視窗
#window.iconbitmap('icon.ico')# 設定程式的圖示，可在括弧中放入檔案路徑

def hello():
    print("Hello, world.")

def onOK():
    # 取得輸入文字
    print("Hello, {}.".format(entry.get()))
    window.destroy()#關閉螢幕
    
#def onOK():
    #msg = "Hello, {}.".format(entry.get())
    #tkinter.messagebox.showinfo(title = 'Hello', # 視窗標題
                               # message = msg)   # 訊息內容

#test.pack(side="top",fill="x")#這個參數用來調整元件填滿的屬性，有x、y、both可用



# 建立按鈕
#button = tk.Button(window,          # 按鈕所在視窗
                   #text = 'Hello',  # 顯示文字
                   #command = hello) # 按下按鈕所執行的函數


# 標示文字
#label = tk.Label(window,                 # 文字標示所在視窗
                 #text = 'Hello, world',  # 顯示文字
                 #bg = '#EEBB00',         #  背景顏色
                 #font = ('Arial', 12),   # 字型與大小
                 #width = 15, height = 2) # 文字標示尺寸   




# 以預設方式排版標示文字
#label.pack()



# 標示文字
label = tk.Label(window, text = '姓名')
label.pack()

# 輸入欄位
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
entry.pack()

button = tk.Button(window, text = "OK", command = onOK)

# 以預設方式排版按鈕
button.pack()



window.mainloop()

print("this is test ")



















