from PIL import Image  #Импортируем модуль Image из библиотеки PIL для обработки изображений
from .imageProcessor import *  #Импортируем все из локального модуля imageProcessor
import os  #Импортируем модуль os для работы с файловой системой


class ImageHandler():  #Определяем класс ImageHandler
    def __init__(self):  #Метод инициализации
        self.img = None  #Инициализируем переменную для хранения изображения
        self.file_path = None  #Инициализируем переменную для хранения пути к файлу

    def load_image(self, file_path):  #Метод для загрузки изображения
        self.img = Image.open(file_path)  #Открываем изображение по заданному пути и сохраняем в переменную img
        
    def re_size(self):  #Метод для изменения размера изображения
        max_size = (200, 200)  #Устанавливаем максимальный размер
        self.img.thumbnail(max_size)  #Изменяем размер изображения до максимального размера

    def save_to_file(self, file_path, name):  #Метод для сохранения изображения в файл
        self.img.save(file_path)  #Сохраняем изображение по заданному пути
        os.rename(file_path, name)  #Переименовываем файл в заданное имя
    
    def countor_load(self):  #Метод для применения контура к изображению
        filter = ImageProcessor(self.img)  #Создаем объект класса ImageProcessor
        self.img = filter.contour(self.img)  #Применяем метод контурирования и сохраняем результат в img

    def text_var_load(self):  #Метод для добавления текста к изображению
        filter = ImageProcessor(self.img)  #Создаем объект класса ImageProcessor
        self.img = filter.text_var()  #Применяем метод text_var и сохраняем результат в img
