import random
import tkinter as tk
import pandas as pd
import datetime
def Checklove():
	global result
	text_area = tk.Text(master=root,height=2,width=60,bg="red")
	text_area.grid(column=0,row=5)
	result=("friendship score is :",result)
	text_area.insert(tk.END,result)


root = tk.Tk()
root.geometry("400x300")
root.title("Friendship Calculator Game")
result=40+int(pd.datetime.now().second)
entryname1 = tk.Entry(root,width=20,textvariable='name1')
entryname1.grid(column=1,row=1)
entryname2 = tk.Entry(root,width=20,textvariable='name2')
entryname2.grid(column=1,row=2)
button2 = tk.Button(text="   CHECK LOVE     ", bg="pink" , command = Checklove)
button2.grid(column=1,row=3)
label1 = tk.Label(root,text='your name: ',bg='blue',font=('',15,'bold'))
label1.grid(row=1,column=0,pady=5,padx=5)
label2 = tk.Label(root,text='friend name: ',bg='blue',font=('',15,'bold'))
label2.grid(row=3,column=0,pady=5,padx=5)

root.mainloop()
 

