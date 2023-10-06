import tkinter as tk
from tkinter import ttk

root = tk.Tk ()
style = ttk.Style()

root.title("Mi primer ventana!")

canvas=tk.Canvas(root,bg="lightgray",width=1720,height=800)
canvas.pack(fill="both",expand=True)

div = tk.Button(canvas,bg="purple",width=200,height=200,highlightbackground="white", highlightthickness=2)
div.grid(row=0,column=0)
divTable=[]
for i in range(3):
    for j in range(3):
        frame=tk.Button(div,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)
div2=tk.Button(canvas,bg="blue",width=200,height=200,highlightbackground="white",highlightthickness=2)
div2.grid(row=0,column=1)

for i in range(3):
    for j in range(3):
        frame=tk.Button(div2,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)
div3=tk.Button(canvas,bg="green",width=200,height=200,highlightbackground="white",highlightthickness=2)
div3.grid(row=0,column=2)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div3,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)

div4=tk.Button(canvas,bg="skyblue",width=200,height=200,highlightbackground="white",highlightthickness=2)
div4.grid(row=1,column=0)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div4,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)

div5=tk.Button(canvas,bg="purple",width=200,height=200,highlightbackground="white",highlightthickness=2)
div5.grid(row=1,column=1)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div5,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)

div6=tk.Button(canvas,bg="blue",width=200,height=200,highlightbackground="white",highlightthickness=2)
div6.grid(row=1,column=2)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div6,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)
div7=tk.Button(canvas,bg="blue",width=200,height=200,highlightbackground="white",highlightthickness=2)
div7.grid(row=2,column=0)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div7,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)
div8=tk.Button(canvas,bg="blue",width=200,height=200,highlightbackground="white",highlightthickness=2)
div8.grid(row=2,column=1)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div8,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)
div9=tk.Frame(canvas,bg="blue",width=200,height=200,highlightbackground="white",highlightthickness=2)
div9.grid(row=2,column=2)
for i in range(3):
    for j in range(3):
        frame=tk.Button(div9,bg="gray",highlightbackground="white",highlightthickness=2,width=65,height=65)
        frame.grid(row=i,column=j)

tk.mainloop()