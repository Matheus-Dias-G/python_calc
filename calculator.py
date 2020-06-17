from tkinter import *

class Calculator:
    def __init__(self, father):
        self.father = father
        self.father.title('calculator')
        self.father.rowconfigure(0, weight = 1)
        self.father.columnconfigure(0, weight = 1)


        exp = ''
        def rec_num(num):
            global exp
            exp += str(num)
            x.set(exp)
            print(exp)


        x = StringVar()
        self.entry = Entry(self.father, state='readonly' ,textvariable = x)
        self.entry.grid(row=2, columnspan=3, sticky= 'W'+'E'+'N'+'S')

        #Buttons
        self.bt_seven = Button(self.father, text=7, width=10, command = lambda : rec_num(7))
        self.bt_seven.grid(row=3, column=0, sticky = 'W'+'E'+'N'+'S')


        self.bt_eight = Button(self.father, text=8, width=10, command = lambda : rec_num(8))
        self.bt_eight.grid(row=3, column=1, sticky= 'W'+'E'+'N'+'S')
        
        self.bt_nine = Button(self.father, text=9, width=10)
        self.bt_nine.grid(row=3, column=2, sticky='W'+'E'+'N'+'S')

        self.bt_four = Button(self.father, text=4, width=10)
        self.bt_four.grid(row=4, column=0, sticky='W'+'E'+'N'+'S')

        self.bt_five = Button(self.father, text=5, width=10)
        self.bt_five.grid(row=4, column=1, sticky='W'+'E'+'N'+'S')

        self.bt_six = Button(self.father, text=6, width=10)
        self.bt_six.grid(row=4, column=2, sticky='W'+'E'+'N'+'S')

        self.bt_one = Button(self.father, text=1, width=10)
        self.bt_one.grid(row=5, column=0, sticky='W'+'E'+'N'+'S')

        self.bt_two = Button(self.father, text=2, width=10)
        self.bt_two.grid(row=5, column=1, sticky='W'+'E'+'N'+'S')

        self.bt_three = Button(self.father, text=3, width=10)
        self.bt_three.grid(row=5, column=2, sticky='W'+'E'+'N'+'S')

        self.mult = Button(self.father, text='*', width=10)
        self.mult.grid(row=2, column=3, sticky='W'+'E'+'N'+'S')

        self.div = Button(self.father, text='/', width=10)
        self.div.grid(row=3, column=3, sticky='W'+'E'+'N'+'S')

        self.sum =  Button(self.father, text='+', width=10)
        self.sum.grid(row=4, column=3, sticky='W'+'E'+'N'+'S')

        self.subtract = Button(self.father, text='-', width=10)
        self.subtract.grid(row=5, column=3)

        self.exit =  Button(self.father, text='exit', command=self.father.quit, width=10)
        self.exit.grid(row=6, column=1)

        self.zero = Button(self.father, text=0, width=10)
        self.zero.grid(row=6, column=0)

        self.point = Button(self.father, text=',', width=10)
        self.point.grid(row=6, column=2, sticky='W'+'E'+'N'+'S')

        self.result = Button(self.father, text='enter', width=10)
        self.result.grid(row=6, column=3, sticky='W'+'E'+'N'+'S')








root =  Tk()
Calculator(root)
root.mainloop()
