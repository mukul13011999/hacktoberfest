from docx2pdf import convert
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
win = tk.Tk()
win.title('Word2PDF_Convertor')

def Conv():
	try:

		path = entry_path.get()
		path1 = entry_path1.get()
		convert(path,path1)
		showinfo("Convert Succesfully","Go To your documents")

	except:
		showinfo("Something went is wrong","try again or check file name")





path_lable =tk.Label(win,text="Enter WordFile path here : ")
path_lable.grid(row=0,column=0)

entry_path =tk.Entry(win,width=30,bg="#69bef6",bd=2)
entry_path.grid(row=0,column=1,padx=5,pady=5)

path_lable1 =tk.Label(win,text="Enter pdf filename here : ")
path_lable1.grid(row=1,column=0)

entry_path1 =tk.Entry(win,width=30,bg="#69bef6",bd=2)
entry_path1.grid(row=1,column=1,padx=5,pady=5)


button= ttk.Button(win,text="Convert",command= Conv)
button.grid(row=2,column=0,columnspan=2)

win.mainloop()