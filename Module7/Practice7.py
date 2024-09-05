import tkinter
import os
from tkinter import filedialog
from tkinter import Menu


def file_select():
    filename = filedialog.askopenfilename(initialdir="/Py", title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '.*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)


def about():
    about_window = tkinter.Tk()
    about_window.title('About')
    about_window.geometry('250x150')
    about_text = tkinter.Label(about_window, text='Создатель: Иван\n'
                                                  'Версия: 0.0.0.01')
    about_text.pack(anchor='nw', expand=1)
    about_window.mainloop()


def info_window():
    inform_window = tkinter.Tk()
    inform_window.title('Info')
    inform_window.geometry('550x150')
    info_text = tkinter.Label(inform_window, text='Пользоваться этим невозможно и делать тут нечего')
    info_text.grid(row=1, column=1)
    inform_window.mainloop()


window = tkinter.Tk()
window.title('Проводник')
window.geometry('550x250')
window.resizable(False, False)
window.configure(bg='gray')


info_menu = Menu(tearoff=0)
info_menu.add_cascade(label='About', command=about)
info_menu.add_cascade(label='Info', command=info_window)


main_menu = Menu()
main_menu.add_cascade(label='Menu', menu=info_menu)


text = tkinter.Label(window, text='Файл: ', width=80, height=5, background='silver')
text.pack(anchor='n', expand=1)
text.pack()

button_select = tkinter.Button(window, width=20, height=3,
                               text='Выберать файл', background='silver', command=file_select)

button_select.pack(anchor='center', expand=1)


window.config(menu=main_menu)




window.mainloop()
