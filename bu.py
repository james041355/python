import tkinter as tk

root = tk.Tk()
root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
#root.iconbitmap('heart_green.ico')
root.geometry('300x200')

def Selection ():
    print(schools [var.get()]) 

schools = {0:"國小",1:"國中",2:"高中",3:"大學",4:"碩士/博士"}


var = tk.IntVar()

var.set(0)
#![https://ithelp.ithome.com.tw/upload/images/20210927/20140047IaqAJzeYOX.png](https://ithelp.ithome.com.tw/upload/images/20210927/20140047IaqAJzeYOX.png)
l = tk.Label(root, text="最高學歷" ,fg="#8B008B", bg="#7AFEC6", width=30)
l.pack()

for val, school in schools.items():
    R=tk.Radiobutton (root,text=school,variable=var, value=val,command=Selection)
    R.pack()

root.mainloop()