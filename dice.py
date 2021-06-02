import random
from tkinter import *
root = Tk()
def roll():
    number=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.config(text=f'{random.choice(number)}{random.choice(number)}',pady="500")
    l1.pack() #pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, #bottom positions offset and relative to each other within a frame.
def biased6():
    number=["\u2680","\u2685","\u2685","\u2681","\u2685","\u2682","\u2683","\u2685","\u2684","\u2685"]
    l1.config(text=f'{random.choice(number)}{random.choice(number)}',pady="500")
    l1.pack() #pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, #bottom positions offset and relative to each other within a frame.
def biased1():
    number=["\u2680","\u2680","\u2685","\u2681","\u2680","\u2682","\u2683","\u2680","\u2684","\u2685"]
    l1.config(text=f'{random.choice(number)}{random.choice(number)}',pady="500")
    l1.pack() #pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, #bottom positions offset and relative to each other within a frame.
root.geometry("700x700")
l1 = Label(root,font=("Helvetical",360))

b0=Button(root,text="A biased die(6). Let's roll...",font=("Helvetical",12),height="3" ,width="25",command=biased6,bg="LightPink1")
b1=Button(root,text="Unbiased dice Let's Roll....",font=("Helvetical",12),height="3",width="25",command=roll,bg="lightCyan")
b2=Button(root,text="A biased die(1). Let's roll...",font=("Helvetical",12),height="3",width="25",command=biased1,bg="pale green")
b0.place(x="10",y="0")
b1.place(x="230",y="0")
b2.place(x="460",y="0")
root.mainloop()