import tkinter as tk  #Импортируем библиотеку tkinter для создания графического интерфейса
from tkinter import ttk  #Импортируем модуль ttk из tkinter для виджетов с темами
from tkinter.messagebox import showerror  #Импортируем showerror для отображения сообщений об ошибках
from tkinter import filedialog as fd  #Импортируем filedialog для работы с диалогами выбора файлов
from tkinter import simpledialog  #Импортируем simpledialog для простых диалогов
from PIL import Image, ImageTk, ImageFilter, ImageFont, ImageDraw  # Импортируем модули из библиотеки PIL для работы с изображениями
import os  #Импортируем библиотеку os для работы с файловой системой

class ImageHandler:  #Определяем класс ImageHandler для обработки изображений
    def __init__(self):  #Метод инициализации класса
        self.img = None  #Инициализируем переменную для хранения изображения
        self.file_path = None  #Инициализируем переменную для хранения пути к файлу

    def load_image(self, file_path):  #Метод для загрузки изображения
        self.img = Image.open(file_path)  #Открываем изображение по указанному пути

    def re_size(self):  #Метод для изменения размера изображения
        max_size = (200, 200)  #Устанавливаем максимальный размер
        self.img.thumbnail(max_size)  #Изменяем размер изображения до максимального размера

    def save_to_file(self, file_path, name):  #Метод для сохранения изображения в файл
        self.img.save(file_path)  #Сохраняем изображение по указанному пути
        new_file_path = f"{name}.png"  #Формируем новое имя файла с расширением .png
        os.rename(file_path, new_file_path)  #Переименовываем файл

    def countor_load(self):  # Метод для применения контура к изображению
        self.img = self.img.filter(ImageFilter.CONTOUR)  #Применяем фильтр контура к изображению

    def text_var_load(self):  #Метод для добавления текста к изображению
        size = self.img.size  #Получаем размеры изображения
        draw = ImageDraw.Draw(self.img)  #Создаем объект для рисования на изображении
        font = ImageFont.truetype("arial.ttf", 24) #Загружаем шрифт Arial с размером 24 для отображения кириллицы
        text = "Вариант 3"  
        bbox = draw.textbbox((0, 0), text, font=font)  #Вычисляем размер текста
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]  #Получаем ширину и высоту текста
        text_x = (size[0] - text_width) / 2  #Вычисляем координату x для центрирования текста
        text_y = (size[1] - text_height) / 2  #Вычисляем координату y для центрирования текста
        draw.text((text_x, text_y), text, font = font)  #Рисуем текст на изображении

class Imagine(tk.Frame, ImageHandler):  #Определяем класс Imagine, который наследует tk.Frame и ImageHandler
    def __init__(self, master = None):  #Метод инициализации класса
        super().__init__(master)  #Вызов инициализатора родительского класса
        self.initUI()  #Инициализация пользовательского интерфейса

    def initUI(self):  #Метод для инициализации пользовательского интерфейса
        self.pack()  #Упаковка фрейма в окно

        #Создание меню
        menu_bar = tk.Menu(self.master)  #Создаем объект меню
        self.master.config(menu = menu_bar)  #Устанавливаем меню в главное окно

        file_menu = tk.Menu(menu_bar, tearoff=0)  #Создаем подменю "Файл"
        file_menu.add_command(label = 'Загрузить', command = self.load_image_gui)  #Добавляем команду для загрузки изображения
        file_menu.add_command(label = 'Сохранить', command = self.save_to_file_gui)  #Добавляем команду для сохранения изображения
        file_menu.add_separator()  #Добавляем разделитель
        file_menu.add_command(label = 'Выход', command = self.master.quit)  # Добавляем команду для выхода из приложения
        menu_bar.add_cascade(label = 'Файл', menu = file_menu)  # Добавляем подменю "Файл" в меню

        edit_menu = tk.Menu(menu_bar, tearoff=0)  #Создаем подменю "Редактировать"
        edit_menu.add_command(label = 'Размер', command = self.re_size_gui)  #Добавляем команду для изменения размера изображения
        edit_menu.add_command(label = 'Контур', command = self.contour_gui)  #Добавляем команду для применения контура к изображению
        edit_menu.add_command(label = 'Текст', command = self.text_var_load_gui)  #Добавляем команду для добавления текста к изображению
        menu_bar.add_cascade(label = 'Редактировать', menu=edit_menu)  #Добавляем подменю "Редактировать" в меню

        self.label_photo = ttk.Label(self) #Создаем метку для отображения изображения
        self.label_photo.pack(pady = 20)  #Упаковываем метку с отступом

        # Загрузка кнопок
        ttk.Button(self, text = 'Загрузить фото', command = self.load_image_gui).pack(fill = tk.X)  #Создаем и упаковываем кнопку для загрузки фото
        ttk.Button(self, text = 'Изменить размер', command = self.re_size_gui).pack(fill = tk.X)  #Создаем и упаковываем кнопку для изменения размера
        ttk.Button(self, text = 'Контур', command = self.contour_gui).pack(fill = tk.X)  #Создаем и упаковываем кнопку для применения контура
        ttk.Button(self, text = 'Добавить текст', command = self.text_var_load_gui).pack(fill = tk.X)  #Создаем и упаковываем кнопку для добавления текста
        ttk.Button(self, text = 'Сохранить', command = self.save_to_file_gui).pack(fill = tk.X)  #Создаем и упаковываем кнопку для сохранения изображения

    def load_image_gui(self):  # Метод для загрузки изображения через графический интерфейс
        self.file_path = fd.askopenfilename(title="Выберите фото для редактирования", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")])  # Диалоговое окно для выбора файла
        try:
            self.load_image(self.file_path)  #Загружаем выбранное изображение
            self.update_label(self.img)  #Обновляем метку с изображением
        except:
            showerror("Ошибка", "Не удалось открыть фото")  #Показ сообщения об ошибке, если изображение не удалось загрузить

    def update_label(self, img):  #Метод для обновления метки с изображением
        self.img_tk = ImageTk.PhotoImage(img)  #Конвертируем изображение в формат PhotoImage
        self.label_photo.config(image=self.img_tk)  #Устанавливаем изображение в метку

    def re_size_gui(self):  #Метод для изменения размера изображения через графический интерфейс
        self.re_size()  #Изменяем размер изображения
        self.update_label(self.img)  #Обновляем метку с изображением

    def contour_gui(self):  #Метод для применения контура к изображению через графический интерфейс
        self.countor_load()  #Применяем контур к изображению
        self.update_label(self.img)  # Обновляем метку с изображением

    def save_to_file_gui(self):  #Метод для сохранения изображения через графический интерфейс
        name = simpledialog.askstring("Введите название файла", "Название файла")  #Диалоговое окно для ввода имени файла
        try:
            self.save_to_file(self.file_path, name)  #Сохраняем изображение с указанным именем
        except:
            showerror("Ошибка", "Не удалось сохранить изображение")  #Показ сообщения об ошибке, если изображение не удалось сохранить

    def text_var_load_gui(self):  #Метод для добавления текста к изображению через графический интерфейс
        self.text_var_load()  #Добавляем текст к изображению
        self.update_label(self.img)  #Обновляем метку с изображением

class Application(tk.Tk):  #Определяем класс Application, который наследует tk.Tk
    def __init__(self):  #Метод инициализации класса
        super().__init__()  #Вызов инициализатора родительского класса
        self.title('Фото - редактор')  #Устанавливаем заголовок окна
        self.geometry('800x600')  #Устанавливаем размеры окна
        first_label = tk.Label(self, text = "Фото", font = 0)  #Создаем метку с текстом "Фото" и шрифтом размера 0
        first_label.pack(padx = 4, pady = 4)  #Упаковываем метку с текстом "Фото" с отступами 4 по осям x и y
        self.image_handler = Imagine(master = self)  #Создаем экземпляр класса Imagine, передавая ему главное окно как master
        self.image_handler.pack(pady = 10, padx = 10)  #Упаковываем обработчик изображений с отступами по осям x и y

app = Application()  #Создаем экземпляр класса Application
app.mainloop()  #Запускаем основной цикл приложения
