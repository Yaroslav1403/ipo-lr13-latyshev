import tkinter as tk  #Импортируем библиотеку tkinter и переименовываем ее в tk для создания графического интерфейса
from tkinter import ttk  #Импортируем модуль ttk из tkinter для виджетов с темами
from tkinter.messagebox import showerror  #Импортируем showerror для отображения сообщений об ошибках
from tkinter import filedialog as fd  #Импортируем модуль filedialog для диалоговых окон и переименовываем его в fd
from tkinter import simpledialog  #Импортируем simpledialog для простых диалоговых окон
from PIL import Image, ImageTk  #Импортируем Image и ImageTk из PIL для обработки изображений
from .imageHandler import ImageHandler  #Импортируем класс ImageHandler из локального модуля

class Imagine(tk.Frame, ImageHandler):  #Определяем класс Imagine, который наследует tk.Frame и ImageHandler
    def __init__(self, master=None):  #Метод инициализации для класса Imagine
        super().__init__(master)  #Вызов инициализатора родительского класса
        self.initUI()  #Инициализация пользовательского интерфейса

    def initUI(self):  #Метод для инициализации пользовательского интерфейса
        self.pack()  #Упаковка фрейма в окно
        
        #Создаем и упаковываем кнопки с соответствующими командами
        ttk.Button(self, text='Файл', command=self.load_image_gui).pack(fill=tk.X)
        ttk.Button(self, text='Размер', command=self.re_size_gui).pack(fill=tk.X)
        ttk.Button(self, text='Сохранить', command=self.save_to_file_gui).pack(fill=tk.X)
        ttk.Button(self, text='Контур', command=self.contour_gui).pack(fill=tk.X)
        ttk.Button(self, text='Текст', command=self.text_var_load_gui).pack(fill=tk.X)
 
        self.label_photo = ttk.Label(self)  #Создаем метку для отображения фото
        self.label_photo.pack(pady=20)  #Упаковываем метку с отступом

    def load_image_gui(self):  #Метод для загрузки изображения через диалоговое окно
        self.file_path = fd.askopenfilename(title="Выберите фото для редактирования", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*")]) 
        try:
            self.load_image(self.file_path)  #Вызов метода load_image из ImageHandler
            self.update_label(self.img)  #Обновление метки с загруженным изображением
        except:
            showerror("Ошибка", "Не удалось открыть фото")  #Отображение сообщения об ошибке, если загрузка не удалась

    def update_label(self, img):  #Метод для обновления метки с новым изображением
        self.img_tk = ImageTk.PhotoImage(img)  #Конвертация изображения в PhotoImage
        self.label_photo.config(image=self.img_tk)  #Настройка метки для отображения изображения

    def re_size_gui(self):  #Метод для изменения размера изображения
        self.re_size()  #Вызов метода re_size из ImageHandler
        self.update_label(self.img)  #Обновление метки с измененным изображением

    def contour_gui(self):  #Метод для применения контура к изображению
        self.countor_load()  #Вызов метода contour_load из ImageHandler
        self.update_label(self.img)  #Обновление метки с изображением после применения контура

    def save_to_file_gui(self):  #Метод для сохранения изображения в файл
        name = simpledialog.askstring("Введите название файла", "Название файла")  #Запрос имени файла
        try:
            self.save_to_file(self.file_path, name)  #Вызов метода save_to_file из ImageHandler
        except:
            showerror("Ошибка", "Не удалось сохранить изображение")  #Отображение сообщения об ошибке, если сохранение не удалось

    def text_var_load_gui(self):  #Метод для загрузки текстовых переменных
        self.text_var_load()  #Вызов метода text_var_load из ImageHandler
        self.update_label(self.img)  #Обновление метки с изображением после загрузки текста
