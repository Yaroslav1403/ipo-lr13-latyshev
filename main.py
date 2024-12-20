from PIL import Image  #Импортируем модуль Image из библиотеки PIL для работы с изображениями
from imag.imageFunction import Imagine  #Импортируем класс Imagine из локального модуля imag.imageFunction
import tkinter as tk  #Импортируем библиотеку tkinter для создания графического интерфейса

class Application(tk.Tk):  #Определяем класс Application, который наследует tk.Tk
    def __init__(self):  #Метод инициализации
        super().__init__()  #Вызов инициализатора родительского класса
        self.title('Фото - редактор')  # Устанавливаем заголовок окна
        first_label = tk.Label(self, text="Фото", font=20)  #Создаем метку с текстом "Фото" и шрифтом размера 20
        first_label.pack(padx=4, pady=4)  #Упаковываем метку с отступами по оси x и y
        self.image_handler = Imagine(master=self)  #Создаем экземпляр класса Imagine и передаем в него мастер-окно
        self.image_handler.pack(pady=10, padx=10)  #Упаковываем обработчик изображений с отступами по оси x и y
        
app = Application()  #Создаем экземпляр класса Application
app.mainloop()  #Запускаем основной цикл приложения
