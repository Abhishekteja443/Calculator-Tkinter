import tkinter as tk
cal=""

def add_to_cal(symbol):
    global cal
    cal+=str(symbol)
    txt_res.delete(1.0,"end")
    txt_res.insert(1.0,cal)

def eval_cal():
    global cal
    try:
        cal=str(eval(cal))
        txt_res.delete(1.0,"end")
        txt_res.insert(1.0,cal)
    except:
        clear()
        txt_res.insert(1.0,"ERROR")

def enter_eval(self):
    try:
        cal=str(eval(txt_res.get(1.0,"end-1c")))
        txt_res.delete(1.0,"end")
        txt_res.insert(1.0,cal)
    except:
        clear()
        txt_res.insert(1.0,"ERROR")
def clear():
    global cal
    cal=""
    txt_res.delete(1.0,"end")


root = tk.Tk()
root.configure(bg="#17161b")
root.geometry("295x275")
txt_res=tk.Text(root,height=2,width=16,font=("Arial",24))
txt_res.grid(columnspan=5)

b1=tk.Button(root,text="1",command=lambda:add_to_cal(1),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b1.grid(row=2,column=1)

b2=tk.Button(root,text="2",command=lambda:add_to_cal(2),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b2.grid(row=2,column=2)

b3=tk.Button(root,text="3",command=lambda:add_to_cal(3),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b3.grid(row=2,column=3)

b4=tk.Button(root,text="4",command=lambda:add_to_cal(4),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b4.grid(row=3,column=1)

b5=tk.Button(root,text="5",command=lambda:add_to_cal(5),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b5.grid(row=3,column=2)

b6=tk.Button(root,text="6",command=lambda:add_to_cal(6),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b6.grid(row=3,column=3)

b7=tk.Button(root,text="7",command=lambda:add_to_cal(7),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b7.grid(row=4,column=1)

b8=tk.Button(root,text="8",command=lambda:add_to_cal(8),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b8.grid(row=4,column=2)

b9=tk.Button(root,text="9",command=lambda:add_to_cal(9),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b9.grid(row=4,column=3)

b0=tk.Button(root,text="0",command=lambda:add_to_cal(0),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
b0.grid(row=5,column=2)

bplus=tk.Button(root,text="+",command=lambda:add_to_cal("+"),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bplus.grid(row=2,column=4)

bminus=tk.Button(root,text="-",command=lambda:add_to_cal("-"),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bminus.grid(row=3,column=4)

bmul=tk.Button(root,text="*",command=lambda:add_to_cal("*"),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bmul.grid(row=4,column=4)

bdiv=tk.Button(root,text="/",command=lambda:add_to_cal("/"),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bdiv.grid(row=5,column=4)

bleftpara=tk.Button(root,text="(",command=lambda:add_to_cal("("),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bleftpara.grid(row=5,column=1)

brightpara=tk.Button(root,text=")",command=lambda:add_to_cal(")"),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
brightpara.grid(row=5,column=3)

bclear=tk.Button(root,text="C",command=clear,width=5,font=("Arial",14),bg="#FFA500",fg="#fff")
bclear.grid(row=6,column=1)

bequal=tk.Button(root,text="=",command=eval_cal,width=5,font=("Arial",14),bg="#00BFFF",fg="#fff")
bequal.grid(row=6,column=2)

bdot=tk.Button(root,text=".",command=lambda:add_to_cal("."),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bdot.grid(row=6,column=3)

bmod=tk.Button(root,text="%",command=lambda:add_to_cal("%"),width=5,font=("Arial",14),bg="#2a2d36",fg="#fff")
bmod.grid(row=6,column=4)

root.bind("<Return>",enter_eval)
root.resizable(False,False)
root.title("Calculator")
root.mainloop()