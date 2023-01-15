import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('300x300')

canvas = tk.Canvas(root, width=300, height=300)  # 加入 Canvas 畫布
canvas.pack()

root.mainloop()