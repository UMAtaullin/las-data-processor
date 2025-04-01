import matplotlib.pyplot as plt
import pandas as pd


def plot_curves(df: pd.DataFrame, curves: list, title: str = "ГИС кривые"):
    """Рисует графики кривых ГИС по глубине."""
    plt.figure(figsize=(10, 6))
    for curve in curves:
        plt.plot(df[curve], df["DEPT"], label=curve)
    plt.gca().invert_yaxis()  # Глубина увеличивается вниз
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
