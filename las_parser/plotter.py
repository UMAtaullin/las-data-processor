import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import os

def plot_curves(df: pd.DataFrame, curves: list, title: str = "ГИС кривые"):
    # Создаем папку 'res', если её нет
    os.makedirs("res", exist_ok=True)

    # Генерируем уникальное имя файла с датой/временем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"res/gis_plot_{timestamp}.png"

    # Строим график
    plt.figure(figsize=(10, 6))
    for curve in curves:
        if curve in df.columns:
            plt.plot(df[curve], df["DEPT"], label=curve)
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.legend()
    plt.grid()

    # Сохраняем в папку res
    plt.savefig(filename, bbox_inches="tight", dpi=300)
    print(f"График сохранён в {filename}")
    plt.close()  # Закрываем фигуру, чтобы не накапливались в памяти
