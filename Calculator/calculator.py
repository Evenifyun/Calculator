import tkinter
import os
import re
from tkinter import *
from tkinter import messagebox
from tkinter import font


class Calculator(object):
    """计算器"""

    def __init__(self):
        self.tk = tkinter.Tk()
        self.tk.title('计算器')  # 设置标题
        self.tk.geometry('400x500+400+100')  # 设置窗口宽高和显示的位置
        self.tk.iconbitmap(os.getcwd() + '/calculator.ico')  # 设置图标
        self.input_list = []  # 显示输入框的列表
        self.mid_str = ''
        self.button_list = ['清空', '退格', 'x²', '/', '1/x', '%', '√', '*', '7', '8', '9', '-', '4', '5', '6', '+', '1',
                            '2', '3', '=',
                            '0', '.']
        # 增加菜单
        self.menuBar = Menu(self.tk)
        self.tk.config(menu=self.menuBar)
        # 设置菜单选项
        aboutMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='帮助', menu=aboutMenu)
        aboutMenu.add_command(label='关于', command=self.about)
        # 字体设置
        self.EntryFont = font.Font(self.tk, size=13)
        self.ButtonFont = font.Font(self.tk, size=12)
        # 面板显示
        self.str_text = tkinter.StringVar()
        self.str_text.set('0')
        self.label = tkinter.Label(self.tk, bg='#F5F5F5', bd='1', fg='black', anchor='e', font=self.EntryFont,
                                   textvariable=self.str_text)
        self.label.place(y=10, width=380, height=50)
        # 按钮设置
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[0],
                                        font=self.ButtonFont, command=self.clear)
        self.NumButton.place(x=30, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[1],
                                        font=self.ButtonFont, command=self.backspace)
        self.NumButton.place(x=110, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[2],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[2]))
        self.NumButton.place(x=190, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[3],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[3]))
        self.NumButton.place(x=270, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[4],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[4]))
        self.NumButton.place(x=30, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[5],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[5]))
        self.NumButton.place(x=110, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[6],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[6]))
        self.NumButton.place(x=190, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[7],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[7]))
        self.NumButton.place(x=270, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[8],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[8]))
        self.NumButton.place(x=30, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[9],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[9]))
        self.NumButton.place(x=110, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[10],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[10]))
        self.NumButton.place(x=190, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[11],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[11]))
        self.NumButton.place(x=270, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[12],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[12]))
        self.NumButton.place(x=30, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[13],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[13]))
        self.NumButton.place(x=110, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[14],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[14]))
        self.NumButton.place(x=190, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[15],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[15]))
        self.NumButton.place(x=270, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[16],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[16]))
        self.NumButton.place(x=30, y=320, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[17],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[17]))
        self.NumButton.place(x=110, y=320, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[18],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[18]))
        self.NumButton.place(x=190, y=320, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[19],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[19]))
        self.NumButton.place(x=270, y=320, width=70, height=115)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[20],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[20]))
        self.NumButton.place(x=30, y=380, width=150, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#F5F5F5', text=self.button_list[21],
                                        font=self.ButtonFont, command=lambda: self.knobDown(self.button_list[21]))
        self.NumButton.place(x=190, y=380, width=70, height=55)

    # 关于作者信息在这里设置
    def about(self):
        messagebox.showinfo('关于', ' 作者：Even \n verion 1.0 \n 感谢您的使用！')

    # 清空
    def clear(self):
        self.input_list = []
        self.mid_str = ''
        self.str_text.set('0')

    # 退格，没有则设置为0
    def backspace(self):
        if self.input_list:
            self.input_list.pop()
            text = ''.join(self.input_list)
            self.str_text.set(text)
            if self.input_list == []:
                self.str_text.set('0')

    # 判断计算符号
    def signCheck(self, sign):
        return sign in self.input_list

    # 检查input_list中是否有'.'
    def checkList(self):
        listSum = ''.join(self.input_list)
        if '.' in listSum:
            listSum = float(listSum)
        else:
            listSum = int(listSum)
        return listSum

    # 添加button
    def addButton(self, button):
        if button == self.button_list[2]:  # 平方
            listSum = self.checkList()
            self.input_list = [str(listSum ** 2)]
        elif button == self.button_list[4]:  # 倒数
            listSum = self.checkList()
            self.input_list = [str(1 / listSum)]
        elif button == self.button_list[5]:  # 百分号
            listSum = self.checkList()
            self.input_list = [str(listSum * 0.01)]
        elif button == self.button_list[6]:  # 开平方根
            listSum = self.checkList()
            self.input_list = [str(listSum ** 0.5)]
        else:
            self.input_list.append(button)
        text = ''.join(self.input_list)
        self.str_text.set(text)

    # 过滤掉输入的非法字符
    def inputCheck(self, input):
        if re.findall(r'[&a-zA-Z<>,?~!@#$";:]', str(input)):
            if input == '1/x' or input == '%' or input == '√' or input == 'x²':
                pass
            else:
                self.str_text.set('非法字符，请重新输入')

    # 按钮事件处理
    def knobDown(self, button):
        self.inputCheck(button)
        # input_list为空时，检查输入的第一位是否为数字
        if self.input_list == [] and button in ['-', '+', '*', '/', '=', '.', '%', '1/x', '√', 'x²']:
            self.str_text.set('符号不能放在第一位哦~')
        # 如果输入算符
        elif button in ['+', '-', '*', '/', '%', '1/x', '√', 'x²']:
            # 判断input_list里面是否有算符
            if self.signCheck('-') or self.signCheck('+') or self.signCheck('/') or self.signCheck('*'):
                if re.findall(r'[-+*/]', str(self.input_list[-1])) or button in ['x²', '1/x', '%', '√']:
                    self.str_text.set('不能连续输入运算符')
                else:
                    self.addButton(button)
            else:
                self.addButton(button)
        elif button == '=':
            if re.findall(r'[-+*/]', str(self.input_list[-1])):
                self.str_text.set('结尾不能是算符哦~')
            else:
                self.mid_str = ''.join(self.input_list)
                self.str_text.set(str(round(eval(self.mid_str),8)))
                self.input_list = []
                self.mid_str = ''
        else:
            self.addButton(button)

    def start(self):
        self.tk.mainloop()


if __name__ == '__main__':
    NewCalculator = Calculator()
    NewCalculator.start()
