#http://www.youtube.com/watch?v=rcACl0sUJeQ&list=PL8BEB66FBE6DB97AF
#criando uma tabela de troco
import sys
from tkinter import *
#definindo funcoes e variaveis.


    
#como criar um menu para um arquivo
#criando a janela

janela = Tk()
ment = IntVar()

def abc():
    x = ment.get() 
    if checkbutton1 == 1:
        notascem = x // 100
        x = x % 100
        y = '%.2f notas de cem reais' % (notascem)
        if notascem > 0:
            label = Label(janela,text= y).grid(row= 3,column= 1)
    if checkbutton2 == 1:
        notas50 = x // 50
        x = x % 50
        y = '%.2f notas de cinquenta reais' % (notas50)
        if notas50 > 0:
            label = Label(janela,text = y).grid(row = 4, column = 1)
    if checkbutton3 == 1:
        notas20 = x // 20
        x = x % 20
        y = ('%.2f notas de vinte reais') % (notas20)
        if notas20 > 0:
            label = Label(janela,text = y).grid(row = 5, column = 1)
    if checkbutton4 == 1:
        notas10 = x // 10
        x = x % 10
        y = ('%.2f notas de dez reais') % (notas10)
        if notas10 > 0:
            label = Label(janela,text = y).grid(row = 6, column = 1)
    if checkbutton5 == 1:
        notas5 = x // 5
        x = x % 5
        y = ('%.2f notas de cinco reais') % (notas5)
        if notas5 > 0:
            label = Label(janela,text = y).grid(row = 7, column = 1)
    if checkbutton6 == 1:
        notas2 = x // 2
        x = x % 2
        y = ('%.2f notas de dois reais') % (notas2)
        if notas2 > 0:
            label = Label(janela,text = y).grid(row = 8, column = 1)
    if checkbutton7 == 1:
        moeda1 = x // 1
        x = x % 1
        y = ('%.2f moeadas de um reais') % (moeda1)
        if moeda1 > 0:
            label = Label(janela,text = y).grid(row = 9, column = 1)
    if checkbutton8 == 1:
        moeda50 = x // 0.5
        x = x % 0.5
        y = ('%.2f moeadas de 50 centavos') % (moeda50)
        if moeda50 > 0:
            label = Label(janela,text = y).grid(row = 10, column = 1)
    if checkbutton9 == 1:
        moeda25 = x // 0.25
        x = x % 0.25
        y = ('%.2f moeadas de 25 centavos') % (moeda25)
        if moeda25 > 0:
            label = Label(janela,text = y).grid(row = 11, column = 1)
    if checkbutton10 == 1:
        moeda10 = x // 0.10
        x = x % 0.10
        y = ('%.2f moeadas de 10 centavos') % (moeda10)
        if moeda10 > 0:
            label = Label(janela,text = y).grid(row = 12, column = 1)
    if checkbutton11 == 1:
        moeda5 = x // 0.05
        x = x % 0.05
        y = ('%.2f moeadas de 5 centavos') % (moeda5)
        if moeda5 > 0:
            label = Label(janela,text = y).grid(row = 13, column = 1)
    return
        


def c1():
    label = Label(janela,text='You Cliked Now',fg = 'blue')
    return
def About():
    messagebox.showinfo(title='About',message = 'It is about nothing')
    return
def fechar():
    fechar = messagebox.askokcancel(title='Quit',message='Voce Realmente deseja sair?')
    if fechar > 0:
        janela.destroy()
        return
    

#colocando o tamanho dela

janela.geometry('600x600+500+300')
janela.title('Janela')

#criando os checksbuttons para as notas e moedas existentes para o troco

checkbutton1 = Checkbutton(janela,text = 'Notas de 100 reais',onvalue = 1,offvalue = 0).grid(row = 3, column = 0,stick = W)
checkbutton2 = Checkbutton(janela,text = 'Notas de 50 reais',onvalue = 1,offvalue = 0).grid(row = 4, column =0,stick = W)
checkbutton3 = Checkbutton(janela,text = 'Notas de 20 reais',onvalue = 1,offvalue = 0).grid(row = 5, column = 0,stick = W)
checkbutton4 = Checkbutton(janela,text = 'Notas de 10 reais',onvalue = 1,offvalue = 0).grid(row = 6, column = 0,stick = W)
checkbutton5 = Checkbutton(janela,text = 'Notas de 5 reais',onvalue = 1,offvalue = 0).grid(row = 7, column = 0,stick = W)
checkbutton6 = Checkbutton(janela,text = 'Notas de 2 reais',onvalue = 1,offvalue = 0).grid(row = 8, column = 0,stick = W)
checkbutton7 = Checkbutton(janela,text = 'Moedas de 1 real',onvalue = 1,offvalue = 0).grid(row = 9, column = 0,stick = W)
checkbutton8 = Checkbutton(janela,text = 'Moedas de 0.50 centavos',onvalue = 1,offvalue = 0).grid(row = 10, column = 0,stick = W)
checkbutton9 = Checkbutton(janela,text = 'Moedas de 0.25 centavos',onvalue = 1,offvalue = 0).grid(row = 11, column = 0,stick = W)
checkbutton10 = Checkbutton(janela,text = 'Moedas de 0.10 centavos',onvalue = 1,offvalue = 0).grid(row = 12, column = 0,stick = W)
checkbutton11 = Checkbutton(janela,text = 'Moedas de 0.5 centavos',onvalue = 1,offvalue = 0).grid(row = 13, column = 0,stick = W)


#criando labels
label1 = Label(janela,text='Arquivo do bruno').grid(row = 0,column = 1,stick = N)
               
#criando botoes

botao1 = Button(janela,text='Aperte',
                command = abc,
                fg = 'red',
                bg = 'yellow')
botao1.grid(row = 1,column = 1,stick = N)

#criando os checksbuttons para as notas e moedas existentes para o troco


#criando entradas de dado

entrada1 = Entry(janela,textvariable = ment).grid(row = 2,column = 1)

#criando um menu
menubar = Menu(janela)
#colocando coisas no menu
aba = Menu(menubar, tearoff = 1)
aba.add_command(label='New',command = c1)#definicao em cima
aba.add_command(label='Open')
aba.add_command(label='Save As...')
aba.add_command(label='Close', command = fechar)#definicao em cima

menubar.add_cascade(label="File",menu = aba)
#criando mais um item para o menubar que tera varios itens como esta depois do aba ele sera colocado em segundo lugar
helpmenu = Menu(menubar,tearoff = 1)
helpmenu.add_command(label='Help Docs')
helpmenu.add_command(label='About',command = About)#definicao em cima

menubar.add_cascade(label='Help',menu = helpmenu)

janela.config(menu = menubar)

janela.mainloop()
