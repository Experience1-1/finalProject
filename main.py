import tkinter as tk
import matplotlib.pyplot as plt

def check_output():
    # Здесь вы можете добавить код, который проверяет вывод вашего визуализатора
    # Например, вы можете проверить, соответствует ли вывод вашего визуализатора ожидаемому выводу

    # Для этого примера мы просто создадим график и покажем его
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.show()

# Создаем главное окно приложения
root = tk.Tk()

# Добавляем кнопку "Проверить вывод"
check_button = tk.Button(root, text="Проверить вывод", command=check_output)
check_button.pack()

# Запускаем приложение
root.mainloop()