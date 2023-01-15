import tkinter as tk
# 引入訊息視窗模組
import tkinter.messagebox

window = tk.Tk()

window.title('Hello World')#程式上方的文字
window.geometry("300x300+250+150")


def hello():
    print("Hello, world.")

def onOK():
    # 取得輸入文字
    if entry.get() == "" :
        #print ("noooo")
        tkinter.messagebox.showinfo(title = 'Hello', # 視窗標題
                                message = "no date")   # 訊息內容
    else:
        print("Hello, {}.".format(entry.get()))
        window.destroy()#關閉螢幕
    





# 標示文字
#label = tk.Label(window,                 # 文字標示所在視窗
                 #text = 'Hello, world',  # 顯示文字
                 #bg = '#EEBB00',         #  背景顏色
                 #font = ('Arial', 12),   # 字型與大小
                 #width = 15, height = 2) # 文字標示尺寸   

#label.pack()



# 標示文字
for i in range(10):

    label = tk.Label(window, text = str(i))
    label.pack()


entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 20) # 輸入欄位的寬度
entry.pack()


button = tk.Button(window, text = "OK", command = onOK)
button.pack()



window.mainloop()

print("this is test ")
