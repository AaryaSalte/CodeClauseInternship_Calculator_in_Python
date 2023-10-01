from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
               
               value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"


        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:    
        scvalue.set(scvalue.get()+text)
        screen.update()
root = Tk()
root.geometry("300x600")
root.title("Simple Calculator")

scvalue= StringVar()
scvalue.set("")
screen= Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f=Frame(root, bg="grey")
b=Button(f, text="9",height=1,width=2,font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="8",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="7",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="*",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root, bg="grey")
b=Button(f, text="6",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="5",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="4",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="-",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root, bg="grey")
b=Button(f, text="3",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="2",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="1",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="+",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root, bg="grey")
b=Button(f, text="C",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="0",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="%",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="=",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root, bg="grey")
b=Button(f, text="(",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text=")",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text=".",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

b=Button(f, text="00",height=1,width=2, font="lucida 35 bold")
b.pack(side=LEFT,padx=1)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()