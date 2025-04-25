from tkinter import *

# Створення головного вікна
root = Tk()
root.title("Міста України")

#Текстове поле для виводу інформації
text1 = Text(width=40, height=15, wrap=WORD)
text1.grid(row=0, column=1, rowspan=7, padx=10, pady=10)

# Змінна для вибору кнопок
var = IntVar()
var.set(0)

#Обробка вибору міста
def change():
    # Список файлів з інформацією про міста (додаємо також улюблені міста)
    files = ['Київ.txt', 'Львів.txt', 'Дніпро.txt', 'Одеса.txt', 'Харків.txt']
    view(files[var.get()]) # Викликаємо відображення відповідного файлу

#Читання даних для відповідного техтового файлу
def view(file_name):
    text1.delete(1.0, END)
    try:
        with open(file_path, encoding='utf-8') as f:
            text1.insert(1.0, f.read())
    except FileNotFoundError:
        text1.insert(1.0, f"Файл '{file_name}' не знайдено.")

#Міста
cities = ['Київ', 'Львів', 'Дніпро', 'Одеса', 'Харків']
for i, city in enumerate(cities):
    rb = Radiobutton(text=city, variable=var, value=i, command=change)
    rb.grid(row=i, column=0, sticky=W)

#Запуск головного циклу
root.mainloop()