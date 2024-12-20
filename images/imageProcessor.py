from PIL import ImageFilter, ImageDraw  #Импортируем модули ImageFilter и ImageDraw из библиотеки PIL

class ImageProcessor:  #Определяем класс ImageProcessor
    def __init__(self, img):  #Метод инициализации
        self.img = img  #Инициализируем переменную для хранения изображения

    def contour(self, img):  #Метод для применения контура к изображению
        self.img = self.img.filter(ImageFilter.CONTOUR)  #Применяем фильтр контура к изображению
        return self.img  #Возвращаем изображение с примененным контуром

    def text_var(self):  #Метод для добавления текста к изображению
        size = self.img.size  #Получаем размер изображения
        draw = ImageDraw.Draw(self.img)  #Создаем объект для рисования на изображении
        draw.text((size[0] / 2, size[1] / 2), 'option 3', fill=('#1C0606'))  #Добавляем текст в центр изображения
        return self.img  #Возвращаем изображение с добавленным текстом
