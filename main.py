from las_parser.parser import load_las, filter_anomalies
from las_parser.plotter import plot_curves

# Загрузка данных
df = load_las("data/example.las")
if df is not None:
    # Фильтрация аномалий (например, RES > 1000 Ом·м)
    df_clean = filter_anomalies(df, "RES", 1000.0)
    # Визуализация
    plot_curves(df_clean, ["GR", "RES", "NPHI"], "Пример обработки LAS")
