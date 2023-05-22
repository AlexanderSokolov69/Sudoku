from tkinter import *
from tkinter.ttk import Radiobutton
import tkinter.ttk as ttk

from const import *


def draw_lines(canv):
    canv.create_line(3, 0, 3, CANV_HEIGHT, fill=COLORS['чёрный'], width=3)
    for num in range(1, 12):
        x = CELL_SIZE * num
        if num % 3 == 0:
            canv.create_line(x, 0, x, CANV_HEIGHT, fill=COLORS['чёрный'], width=3)
        else:
            canv.create_line(x, 0, x, CANV_HEIGHT, fill=COLORS['чёрный'], width=2, dash=(4, 2))
    canv.create_line(0, 3, CANV_WIDTH, 3, fill=COLORS['чёрный'], width=3)
    for num in range(1, 12):
        y = CELL_SIZE * num
        if num % 3 == 0:
            canv.create_line(0, y, CANV_WIDTH, y, fill=COLORS['чёрный'], width=3)
        else:
            canv.create_line(0, y, CANV_WIDTH, y, fill=COLORS['чёрный'], width=2, dash=(4, 2))


class Sudoku(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        ''' Инициализация окна программы и её виджетов '''
        self.master.title('Генератор Судоку')
        self.master.geometry('750x480')
        self.master.resizable(width=False, height=False)
        self.pack(fill=BOTH, expand=1)
        
        frame2 = Frame(self, bg=COLORS['темно-пшеничный'])
        frame2.place(relheight=1, relwidth=0.57)
        
        frame = Frame(self)
        frame.place(relheight=0.76, relwidth=0.485, relx=0.04, rely=0.02)
        
        self.canvas = Canvas(frame)
        draw_lines(self.canvas)
        self.canvas.pack(fill=BOTH, expand=1)
        
        self.but_save = Button(frame2, text='Сохранить', cursor='heart', activebackground=COLORS['чёрный'],
                               activeforeground=COLORS['темно-пшеничный'], bg=COLORS['темно-пшеничный'],
                               font=("Georgia", 20), width=14, state=DISABLED)
        self.but_save.pack(side=BOTTOM, pady=16)
        
        lbframe_right = LabelFrame(text='', bg=COLORS['пшеничный'])
        lbframe_right.place(relheight=1, relwidth=0.45, relx=0.57, rely=0)
        
        tl1 = Label(lbframe_right, text='Генератор Судоку', bg=COLORS['пшеничный'], font=("Arial", 25))
        tl1.pack(pady=15)
        self.but_create = Button(lbframe_right, text='Создать', cursor='heart', activebackground=COLORS['чёрный'],
                                 activeforeground=COLORS['темно-пшеничный'], bg=COLORS['темно-пшеничный'],
                                 font=("Georgia", 20), width=14)
        self.but_create.pack(side=BOTTOM, pady=16)
        
        lbframe1 = LabelFrame(text=' Сложность: ', bg=COLORS['пшеничный'], font=("Georgia", 22))
        lbframe1.place(relheight=0.45, relwidth=0.4, relx=0.59, rely=0.2)
        sty = ttk.Style()
        sty.configure('Wild.TRadiobutton', background=COLORS['пшеничный'], selectcolor=COLORS['темно-пшеничный'],
                      font=("Georgia", 20))
        self.show_result = BooleanVar()
        self.show_result.set(0)
        chk1 = Checkbutton(lbframe_right, text="Показать решение", cursor='heart', bg=COLORS['пшеничный'],
                           variable=self.show_result, onvalue=1, offvalue=0, font=("Georgia", 16),
                           command=None)
        chk1.pack(side=BOTTOM)
        
        self.gr_level = IntVar()
        rad1 = Radiobutton(lbframe1, text='Простая', cursor='heart', style='Wild.TRadiobutton',
                           variable=self.gr_level, value=1)
        rad1.pack(side=TOP, pady=6, padx=74)
        rad2 = Radiobutton(lbframe1, text='Средняя', cursor='heart', style='Wild.TRadiobutton',
                           variable=self.gr_level, value=2)
        rad2.pack(side=TOP, pady=6, padx=74)
        rad3 = Radiobutton(lbframe1, text='Сложная', cursor='heart', style='Wild.TRadiobutton',
                           variable=self.gr_level, value=3)
        rad3.pack(side=TOP, pady=6, padx=(70, 60))
        self.gr_level.set(1)


def main():
    window = Tk()
    ex = Sudoku()
    window.mainloop()


if __name__ == '__main__':
    main()
