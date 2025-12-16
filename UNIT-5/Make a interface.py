import tkinter as tk
root=tk.Tk()
root.geometry("500x400") # you can use (root.minsize(500,400)
l1=tk.Label(text="Enter The First Name:")
l2=tk.Label(text="Enter The Middle Name:")
l3=tk.Label(text="Enter The Last Name:")
t1=tk.Entry(width=30)
t2=tk.Entry(width=30)
t3=tk.Entry(width=30)
l1.grid(row=0,column=0,padx=10,pady=10)
t1.grid(row=0,column=1,padx=10,pady=10)
l2.grid(row=1,column=0,padx=10,pady=10)
t2.grid(row=1,column=1,padx=10,pady=10)
l3.grid(row=2,column=0,padx=10,pady=10)
t3.grid(row=2,column=1,padx=10,pady=10)


root.mainloop()