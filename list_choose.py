import tkinter as tk
import calendar    
    
app = tk.Tk()

buttonX = tk.Button(app, text="Label ", bg="blue", height=5)
buttonX.pack(fill='x')

listboxA = tk.Listbox(app, width=10)
listboxA.pack(fill='both', expand=1)

for i in range(1,13):
    listboxA.insert(tk.END, calendar.month_name[i])
    
app.mainloop()
