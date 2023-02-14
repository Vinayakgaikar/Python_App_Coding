from tkinter import *

def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val=""
    data.set("")

def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)


root=Tk()
root.title("ELECTRONIC CALCULATOR")
root.geometry("361x381+500+200")  #(Here 361=>width, 381=>height)
val=''
data=StringVar()    
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("Ariel",20))
display.grid(row=0,columnspan=4)

## Buttons ##
btn7=Button(root,text="7",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(7))  # To pass arguments(=>7) in function we use lambda  
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('+'))
btn_add.grid(row=1,column=3)

btn4=Button(root,text="4",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('-'))
btn_sub.grid(row=2,column=3)

btn1=Button(root,text="1",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(3))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="x",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('*'))
btn_mul.grid(row=3,column=3)

btnc=Button(root,text="C",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=btnClear)
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick(0))
btn0.grid(row=4,column=1)
btn_eq=Button(root,text="=",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btn_eq.grid(row=4,column=2)
btn_div=Button(root,text="÷",font=("Arial",12,"bold"),bd=12,height=2,width=6,command=lambda : btnClick('/'))
btn_div.grid(row=4,column=3)
root.mainloop()
