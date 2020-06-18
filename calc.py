from tkinter import *

i = ' '
class Calculator:
    def __init__(self, father):
        self.father = father
        self.father.title('calculator')
        self.father.rowconfigure(0, weight = 1)
        self.father.columnconfigure(0, weight = 1)
        
        num_multi = '*' 
        num_divi = '/'
        num_sum = '+'
        num_sub = '-'
        
        def rec_num(num):
            global i
            if num == num_multi or num == num_divi or num == num_sub or num == num_sum:
                i = i +  str(num)
                x.set(num)
            else:
                i = i + str(num)
                x.set(i)
                print(i)    

        def res(nums):
            global i
            clear = ''
            r = ''
            for num in list(i):
                if num == num_sum:
                    num_right = i[(1 + i.index(num_sum))::] # valores a direita da operacao
                    num_left = i[:i.index(num_sum)] #valores a esquerda da operacao
                    x.set(clear)
                    r = int(num_left) + int(num_right)
                    x.set(r)
                elif num == num_multi:
                    num_right = i[(1 + i.index(num_multi))::] # valores a direita da operacao
                    num_left = i[:i.index(num_multi)] #valores a esquerda da operacao
                    x.set(clear)
                    r =  int(num_left) * int(num_right)
                    x.set(r)
                elif num == num_divi:
                    num_right = i[(1 + i.index(num_divi))::] # valores a direita da operacao
                    num_left = i[:i.index(num_divi)] #valores a esquerda da operacao
                    x.set(clear)
                    r =  int(num_left) / int(num_right)
                    x.set(r)
                elif num == num_sub:
                    num_right = i[(1 + i.index(num_sub))::] # valores a direita da operacao
                    num_left = i[:i.index(num_sub)] #valores a esquerda da operacao
                    x.set(clear)
                    r =  int(num_left) - int(num_right)
                    x.set(r)

        x = StringVar()
        self.entry = Entry(self.father, state='readonly' ,textvariable = x)
        self.entry.grid(row=2, columnspan=3, sticky= 'W'+'E'+'N'+'S')

        #Buttons
        self.bt_seven = Button(self.father, text=7, width=10, command=lambda : rec_num(7))
        self.bt_seven.grid(row=3, column=0, sticky = 'W'+'E'+'N'+'S')


        self.bt_eight = Button(self.father, text=8, width=10, command=lambda : rec_num(8))
        self.bt_eight.grid(row=3, column=1, sticky= 'W'+'E'+'N'+'S')
        
        self.bt_nine = Button(self.father, text=9, width=10, command=lambda : rec_num(9))
        self.bt_nine.grid(row=3, column=2, sticky='W'+'E'+'N'+'S')
        
        self.bt_four = Button(self.father, text=4, width=10, command=lambda : rec_num(4))
        self.bt_four.grid(row=4, column=0, sticky='W'+'E'+'N'+'S')

        self.bt_five = Button(self.father, text=5, width=10, command=lambda : rec_num(5))
        self.bt_five.grid(row=4, column=1, sticky='W'+'E'+'N'+'S')

        self.bt_six = Button(self.father, text=6, width=10, command=lambda :  rec_num(6))
        self.bt_six.grid(row=4, column=2, sticky='W'+'E'+'N'+'S')

        self.bt_one = Button(self.father, text=1, width=10, command=lambda :  rec_num(1))
        self.bt_one.grid(row=5, column=0, sticky='W'+'E'+'N'+'S')

        self.bt_two = Button(self.father, text=2, width=10, command=lambda : rec_num(2))
        self.bt_two.grid(row=5, column=1, sticky='W'+'E'+'N'+'S')

        self.bt_three = Button(self.father, text=3, width=10, command=lambda : rec_num(3))
        self.bt_three.grid(row=5, column=2, sticky='W'+'E'+'N'+'S')

        self.mult = Button(self.father, text='*', width=10, command=lambda : rec_num('*'))
        self.mult.grid(row=2, column=3, sticky='W'+'E'+'N'+'S')

        self.div = Button(self.father, text='/', width=10, command=lambda : rec_num('/'))
        self.div.grid(row=3, column=3, sticky='W'+'E'+'N'+'S')

        self.sum =  Button(self.father, text='+', width=10, command=lambda : rec_num('+'))
        self.sum.grid(row=4, column=3, sticky='W'+'E'+'N'+'S')

        self.subtract = Button(self.father, text='-', width=10, command=lambda : rec_num('-'))
        self.subtract.grid(row=5, column=3)

        self.exit =  Button(self.father, text='exit', command=self.father.quit, width=10)
        self.exit.grid(row=6, column=1)

        self.zero = Button(self.father, text=0, width=10, command=lambda : rec_num(0))
        self.zero.grid(row=6, column=0)

        self.point = Button(self.father, text=',', width=10)
        self.point.grid(row=6, column=2, sticky='W'+'E'+'N'+'S')

        self.result = Button(self.father, text='enter', width=10, command=lambda : res(i))
        self.result.grid(row=6, column=3, sticky='W'+'E'+'N'+'S')

root =  Tk()
Calculator(root)
root.mainloop()

i = ' '

