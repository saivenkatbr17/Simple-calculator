import tkinter as t
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_filed()
        text_result.insert(1.0, "ERROR")

def clear_filed():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root=t.Tk()
root.geometry("300x275")
text_result = t.Text(root, height=2,width=16, font=("Arial",24))
text_result.grid(columnspan=5)
bt1 = t.Button(root, text="1", command=lambda:add_to_calculation(1), width=5 ,font=("Arial",14))
bt1.grid(row=2,column=1)
bt2 = t.Button(root, text="2", command=lambda:add_to_calculation(2), width=5 ,font=("Arial",14))
bt2.grid(row=2,column=2)
bt3 = t.Button(root, text="3", command=lambda:add_to_calculation(3), width=5 ,font=("Arial",14))
bt3.grid(row=2,column=3)
bt4 = t.Button(root, text="+", command=lambda:add_to_calculation("+"), width=5 ,font=("Arial",14))
bt4.grid(row=2,column=4)
bt5 = t.Button(root, text="4", command=lambda:add_to_calculation(4), width=5 ,font=("Arial",14))
bt5.grid(row=3,column=1)
bt6 = t.Button(root, text="5", command=lambda:add_to_calculation(5), width=5 ,font=("Arial",14))
bt6.grid(row=3,column=2)
bt7 = t.Button(root, text="6", command=lambda:add_to_calculation(6), width=5 ,font=("Arial",14))
bt7.grid(row=3,column=3)
bt8 = t.Button(root, text="-", command=lambda:add_to_calculation("-"), width=5 ,font=("Arial",14))
bt8.grid(row=3,column=4)
bt9 = t.Button(root, text="7", command=lambda:add_to_calculation(7), width=5 ,font=("Arial",14))
bt9.grid(row=4,column=1)
bt10 = t.Button(root, text="8", command=lambda:add_to_calculation(8), width=5 ,font=("Arial",14))
bt10.grid(row=4,column=2)
bt11 = t.Button(root, text="9", command=lambda:add_to_calculation(9), width=5 ,font=("Arial",14))
bt11.grid(row=4,column=3)
bt12 = t.Button(root, text="*", command=lambda:add_to_calculation("*"), width=5 ,font=("Arial",14))
bt12.grid(row=4,column=4)
bt13 = t.Button(root, text="(", command=lambda:add_to_calculation("("), width=5 ,font=("Arial",14))
bt13.grid(row=5,column=1)
bt14 = t.Button(root, text="0", command=lambda:add_to_calculation(0), width=5 ,font=("Arial",14))
bt14.grid(row=5,column=2)
bt15 = t.Button(root, text=")", command=lambda:add_to_calculation(")"), width=5 ,font=("Arial",14))
bt15.grid(row=5,column=3)
bt16 = t.Button(root, text="/", command=lambda:add_to_calculation("/"), width=5 ,font=("Arial",14))
bt16.grid(row=5,column=4)
bt17 = t.Button(root, text="=", command=evaluate_calculation, width=12 ,font=("Arial",14))
bt17.grid(row=6,column=1,columnspan=2)
bt18 = t.Button(root, text="C", command=clear_filed, width=12 ,font=("Arial",14))
bt18.grid(row=6,column=3,columnspan=2)


root.mainloop()
