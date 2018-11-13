#calculadora Tkinter
#feito por deukaus

from tkinter import *
from tkinter import ttk

class Calculadora:
    def __init__(self, janela):
        """ <head> """
        janela.title('Calculadora')
        janela['bg'] = 'white'
        """ </head> """
        self.entry1msg = StringVar()
        self.mensagem = ''

        self.entry1 = Entry(janela, font='bold 20 bold', bg='white', width=16, justify='right', relief='sunken', textvariable = self.entry1msg)
        self.entry1.grid(column=0,row=0, columnspan=4)

        self.button1 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text='(', fg='black', width = 3,height=1, command=self.pareleft)
        self.button1.grid(column='0', row='1')

        self.button2 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text=')', fg='black', width = 3, height=1, command=self.pareright)
        self.button2.grid(column='1', row='1')

        self.button3 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '%', fg='black', width = 3, height=1, command=self.modd)
        self.button3.grid(column="2", row="1")

        self.button4 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = 'C', fg = 'black',width = 3,height = 1, command=self.deletar)
        self.button4.grid(column="3", row="1")

        self.btn_num1 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '1', fg = 'black', width = 3, height = 1, command=self.numero1)
        self.btn_num1.grid(column='0', row='2')

        self.btn_num2 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '2', fg = 'black', width = 3, height = 1, command=self.numero2)
        self.btn_num2.grid(column='1', row='2')

        self.btn_num3 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '3', fg = 'black', width = 3, height = 1, command=self.numero3)
        self.btn_num3.grid(column='2', row='2')

        self.btn_num4 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '4', fg = 'black', width = 3, height = 1, command=self.numero4)
        self.btn_num4.grid(column='0', row='3')

        self.btn_num5 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '5', fg = 'black', width = 3, height = 1, command=self.numero5)
        self.btn_num5.grid(column='1', row='3')

        self.btn_num6 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '6', fg = 'black', width = 3, height = 1, command=self.numero6)
        self.btn_num6.grid(column='2', row='3')

        self.btn_num7 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '7', fg = 'black', width = 3, height = 1, command=self.numero7)
        self.btn_num7.grid(column='0', row='4')

        self.btn_num8 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '8', fg = 'black', width = 3, height = 1, command = self.numero8)
        self.btn_num8.grid(column='1', row='4')

        self.btn_num9 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '9', fg = 'black', width = 3, height = 1, command = self.numero9)
        self.btn_num9.grid(column='2', row='4')

        self.btn_div = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '/', fg = 'black', width = 3, height = 1, command = self.div)
        self.btn_div.grid(column='3', row='2')

        self.btn_mult = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = 'x', fg = 'black', width = 3, height = 1, command = self.mult)
        self.btn_mult.grid(column='3', row='3')

        self.btn_sub = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '-', fg = 'black', width = 3, height = 1, command = self.sub)
        self.btn_sub.grid(column='3', row='4')

        self.btn_add = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '+', fg ='black', width = 3, height = 1, command = self.add)
        self.btn_add.grid(column='3', row='5')

        self.btn_num0 = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '0', fg = 'black', width = 3, height = 1, command = self.numero0)
        self.btn_num0.grid(column='0', row='5')

        self.btn_dot = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '.', fg = 'black', width = 3, height = 1, command = self.dot)
        self.btn_dot.grid(column='1', row='5')

        self.btn_equal = Button(janela, font='bold 20 bold', bg='#E0E0E0', text = '=', fg = 'black', width = 3, height = 1, command = self.equal)
        self.btn_equal.grid(column='2', row='5')
        
    def numero1(self):
        self.mensagem = self.mensagem + '1'
        self.entry1msg.set(self.mensagem)

    def numero2(self):
        self.mensagem = self.mensagem + '2'
        self.entry1msg.set(self.mensagem)

    def numero3(self):
        self.mensagem = self.mensagem + '3'
        self.entry1msg.set(self.mensagem)

    def numero4(self):
        self.mensagem = self.mensagem + '4'
        self.entry1msg.set(self.mensagem)

    def numero5(self):
        self.mensagem = self.mensagem + '5'
        self.entry1msg.set(self.mensagem)

    def numero6(self):
        self.mensagem = self.mensagem + '6'
        self.entry1msg.set(self.mensagem)

    def numero7(self):
        self.mensagem = self.mensagem + '7'
        self.entry1msg.set(self.mensagem)

    def numero8(self):
        self.mensagem = self.mensagem + '8'
        self.entry1msg.set(self.mensagem)

    def numero9(self):
        self.mensagem = self.mensagem + '9'
        self.entry1msg.set(self.mensagem)

    def numero0(self):
        self.mensagem = self.mensagem + '0'
        self.entry1msg.set(self.mensagem)

    def pareleft(self):
        self.mensagem = self.mensagem + '('
        self.entry1msg.set(self.mensagem)

    def pareright(self):
        self.mensagem = self.mensagem + ')'
        self.entry1msg.set(self.mensagem)
    
    def modd(self):
        if self.mensagem[len(self.mensagem)-1] != '%' and self.mensagem[len(self.mensagem)-1] != '+' and self.mensagem[len(self.mensagem)-1] != '-' and self.mensagem[len(self.mensagem)-1] != '/' and self.mensagem[len(self.mensagem)-1] != '*':
            self.mensagem = self.mensagem + '%'
            self.entry1msg.set(self.mensagem)

    def deletar(self):
        self.mensagem = self.mensagem[0:len(self.mensagem) - 1]
        self.entry1msg.set(self.mensagem)

    def div(self):
        if self.mensagem[len(self.mensagem)-1] != '%' and self.mensagem[len(self.mensagem)-1] != '+' and self.mensagem[len(self.mensagem)-1] != '-' and self.mensagem[len(self.mensagem)-1] != '/' and self.mensagem[len(self.mensagem)-1] != '*' and self.mensagem[len(self.mensagem)-1] != '.':
            self.mensagem = self.mensagem + '/'
            self.entry1msg.set(self.mensagem)

    def mult(self):
        if self.mensagem[len(self.mensagem)-1] != '%' and self.mensagem[len(self.mensagem)-1] != '+' and self.mensagem[len(self.mensagem)-1] != '-' and self.mensagem[len(self.mensagem)-1] != '/' and self.mensagem[len(self.mensagem)-1] != '*' and self.mensagem[len(self.mensagem)-1] != '.':
            self.mensagem = self.mensagem + '*'
            self.entry1msg.set(self.mensagem)

    def sub(self):
        if self.mensagem[len(self.mensagem)-1] != '%' and self.mensagem[len(self.mensagem)-1] != '+' and self.mensagem[len(self.mensagem)-1] != '-' and self.mensagem[len(self.mensagem)-1] != '/' and self.mensagem[len(self.mensagem)-1] != '*' and self.mensagem[len(self.mensagem)-1] != '.':
            self.mensagem = self.mensagem + '-'
            self.entry1msg.set(self.mensagem)

    def add(self):
        if self.mensagem[len(self.mensagem)-1] != '%' and self.mensagem[len(self.mensagem)-1] != '+' and self.mensagem[len(self.mensagem)-1] != '-' and self.mensagem[len(self.mensagem)-1] != '/' and self.mensagem[len(self.mensagem)-1] != '*' and self.mensagem[len(self.mensagem)-1] != '.':
            self.mensagem = self.mensagem + '+'
            self.entry1msg.set(self.mensagem)

    def dot(self):
        if self.mensagem[len(self.mensagem)-1] != '%' and self.mensagem[len(self.mensagem)-1] != '+' and self.mensagem[len(self.mensagem)-1] != '-' and self.mensagem[len(self.mensagem)-1] != '/' and self.mensagem[len(self.mensagem)-1] != '*' and self.mensagem[len(self.mensagem)-1] != '.':
            self.mensagem = self.mensagem + '.'
            self.entry1msg.set(self.mensagem)

    def equal(self):
        try:
            self.r = eval(self.mensagem)
            self.mensagem = str(self.r)
            self.entry1msg.set(self.mensagem)
        except:
            self.entry1msg.set('ERROR!!!')
            

root = Tk()
Calculadora(root)
root.mainloop()
