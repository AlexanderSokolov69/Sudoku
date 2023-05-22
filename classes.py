from random import randint, randrange, choices, choice
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import Radiobutton

from const import *


class Sudoku(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ''' Инициализация окна программы и её виджетов '''
        self.field = []
        self.shakes = [self.shake1, self.shake2, self.shake3]
        
        self.master.title('Генератор Судоку')
        self.master.geometry('750x480')
        self.master.resizable(width=False, height=False)
        self.pack(fill=BOTH, expand=1)
        
        frame2 = Frame(self, bg=COLORS['темно-пшеничный'])
        frame2.place(relheight=1, relwidth=0.57)
        
        self.frame = Frame(self)
        self.frame.place(relheight=0.76, relwidth=0.485, relx=0.04, rely=0.02)
        
        self.canvas = Canvas(self.frame)
        self.draw_lines()
        self.canvas.pack(fill=BOTH, expand=1)


        self.but_save = Button(frame2, text='Сохранить', cursor='heart', activebackground=COLORS['чёрный'],
                               activeforeground=COLORS['темно-пшеничный'], bg=COLORS['темно-пшеничный'],
                               font=("Georgia", 20), width=14, state=DISABLED,
                               command=self.save_to_file)
        self.but_save.pack(side=BOTTOM, pady=16)
        
        lbframe_right = LabelFrame(text='', bg=COLORS['пшеничный'])
        lbframe_right.place(relheight=1, relwidth=0.45, relx=0.57, rely=0)
        
        tl1 = Label(lbframe_right, text='Генератор Судоку', bg=COLORS['пшеничный'], font=("Arial", 25))
        tl1.pack(pady=15)
        self.but_create = Button(lbframe_right, text='Создать', cursor='heart', activebackground=COLORS['чёрный'],
                                 activeforeground=COLORS['темно-пшеничный'], bg=COLORS['темно-пшеничный'],
                                 font=("Georgia", 20), width=14,
                                 command=self.make_base)
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
                           command=self.change_view)
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

    def change_view(self):
        if self.field:
            self.show_field()

    def draw_lines(self):
        canv = self.canvas
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

    def make_base(self):
        self.field = []
        for skip in range(9):
            line = [[(x + skip * 3 + skip // 3) % 9 + 1, True, None] for x in range(9)]
            self.field.append(line)
        count = randint(*LEVEL[self.gr_level.get() - 1])
        while count > 0:
            row = randint(0, 8)
            col = randint(0, 8)
            if self.field[row][col][1]:
                self.field[row][col][1] = False
                count -= 1
        self.super_shake()
        if self.field:
            self.but_save['state'] = NORMAL
        self.show_field()
        
    def super_shake(self):
        for _ in range(50):
            self.field = choice(self.shakes)()

    def show_field(self):
        self.frame = Frame(self)
        self.frame.place(relheight=0.76, relwidth=0.485, relx=0.04, rely=0.02)
        self.canvas = Canvas(self.frame)
        self.draw_lines()
        self.canvas.pack(fill=BOTH, expand=1)

        for row in range(9):
            for col in range(9):
                if self.field[row][col][1] or self.show_result.get():
                    numb_frame = LabelFrame(self.frame, borderwidth=0)
                    numb_frame.place(relheight=0.08, relwidth=0.08,
                                     relx=0.02 + col * 0.11,
                                     rely=0.02 + row * 0.11)
                    num = Label(numb_frame, text=str(self.field[row][col][0]),
                                font=("Arial", 25))
                    num.pack()
                    self.field[row][col][2] = (numb_frame, num)
                    
    def shake1(self):
        new_field = []
        for i in range(9):
            line = []
            for j in range(9):
                line.append(self.field[j][i])
            new_field.append(line)
        return new_field
    
    def shake2(self):
        new_field = self.field.copy()
        row_col = randint(0, 1)
        region = randint(0, 2)
        lines = choices([0, 1, 2], k=2)
        xrow = row_col
        xcol = (row_col + 1) % 1
        for n in range(9):
            new_field[(n * xrow) + (region * 3 + lines[0]) * xcol][(n * xcol) + (region * 3 + lines[0]) * xrow],\
            new_field[(n * xrow) + (region * 3 + lines[1]) * xcol][(n * xcol) + (region * 3 + lines[1]) * xrow] = \
            new_field[(n * xrow) + (region * 3 + lines[1]) * xcol][(n * xcol) + (region * 3 + lines[1]) * xrow], \
            new_field[(n * xrow) + (region * 3 + lines[0]) * xcol][(n * xcol) + (region * 3 + lines[0]) * xrow]
        return new_field
    
    def shake3(self):
        new_field = self.field.copy()
        row_col = randint(0, 1)
        lines = choices([0, 1, 2], k=2)
        xrow = row_col
        xcol = (row_col + 1) % 1
        for n in range(9):
            for shift in range(3):
                new_field[(n * xrow) + (shift + lines[0] * 3) * xcol][(n * xcol) + (shift + lines[1] * 3) * xrow], \
                new_field[(n * xrow) + (shift + lines[1] * 3) * xcol][(n * xcol) + (shift + lines[0] * 3) * xrow] = \
                new_field[(n * xrow) + (shift + lines[1] * 3) * xcol][(n * xcol) + (shift + lines[0] * 3) * xrow], \
                new_field[(n * xrow) + (shift + lines[0] * 3) * xcol][(n * xcol) + (shift + lines[1] * 3) * xrow]
        return new_field
    
    def save_to_file(self):
        print('SAVE')
