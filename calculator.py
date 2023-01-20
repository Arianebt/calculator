from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = " "
    text_Input.set(" ")


def btnAddition():
    global operator
    operator = "+"
    text_Input.set()


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


cal = Tk()
cal.title = ("calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input,
                   bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

btnclear = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="C", command=btnClearDisplay).grid(row=1, column=0)

btnpercent = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                    text="%").grid(row=1, column=1)

btndivider = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                    text="/", command=lambda: btnClick("/")).grid(row=1, column=2)

btndel = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text="<-", command=lambda: btnClick()).grid(row=1, column=3)

btn1 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", command=lambda: btnClick(1)).grid(row=2, column=0)

btn2 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", command=lambda: btnClick(2)).grid(row=2, column=1)

btn3 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", command=lambda: btnClick(3)).grid(row=2, column=2)

btnplus = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="+", command=lambda: btnClick('+')).grid(row=2, column=3)

btn4 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", command=lambda: btnClick(6)).grid(row=3, column=2)

btnminus = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="-", command=lambda: btnClick('-')).grid(row=3, column=3)

btn7 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", command=lambda: btnClick(7)).grid(row=4, column=0)

btn8 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", command=lambda: btnClick(8)).grid(row=4, column=1)

btn9 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", command=lambda: btnClick(9)).grid(row=4, column=2)

btntimes = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", command=lambda: btnClick('*')).grid(row=4, column=3)

btncomma = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text=",", command=lambda: btnClick(",")).grid(row=5, column=0)

btn0 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", command=lambda: btnClick(0)).grid(row=5, column=1)

btndot = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                text=".", command=lambda: btnClick(".")).grid(row=5, column=2)

btnequal = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="=", command=btnEqualsInput).grid(row=5, column=3)


cal.mainloop()
