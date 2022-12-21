from tkinter import Tk, Label, CENTER, Entry, Button
from tkinter import messagebox

# Основные настройки окна
window = Tk()
# Название окна
window.title('Авторизация')
# Размер окна
window.geometry('450x230')
window.resizable(False, False)
# Шрифты и размеры текста
font_header = ('TimesNewRoman', 15)
font_entry = ('TimesNewRoman', 12)
label_font = ('TimesNewRoman', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# Создания основной начинки:
# Текста по центру экрана Авторизация.
main_label = Label(window, text='Авторизация', font=font_header,
                   justify=CENTER, **header_padding)
main_label.pack()
# Текста над первой строкой ввода
username_label = Label(window, text='Имя пользователя', font=label_font,
                       **base_padding)
username_label.pack()
# Строка ввода
username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()
# Текста над второй строкой ввода
password_label = Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()
# Строка ввода
password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()


# Метод получения логина и пароля
def clicked():
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo('Заголовок',
                        '{username}, {password}'.format(username=username,
                                                        password=password))


# Создана кнопка, при нажатии которой будет вызван метод clicked

send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()
