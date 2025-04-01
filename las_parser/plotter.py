import matplotlib.pyplot as plt
import pandas as pd


def plot_curves(df: pd.DataFrame, curves: list, title: str = "ГИС кривые"):
    """Рисует графики кривых ГИС по глубине."""
    plt.figure(figsize=(10, 6))
    for curve in curves:
        if curve in df.columns:
            plt.plot(df[curve], df["DEPT"], label=curve)
        else:
            print(f"Пропущена кривая '{curve}'. Доступные: {list(df.columns)}")
    plt.gca().invert_yaxis()
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig("gis_plot.png")  # Сохраняем в файл
    print("График сохранён в gis_plot.png")  # Уведомление в консоль
