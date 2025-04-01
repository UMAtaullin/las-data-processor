import lasio
import pandas as pd
from typing import Optional


def load_las(file_path: str) -> Optional[pd.DataFrame]:
    """Загружает LAS-файл и возвращает DataFrame с кривыми ГИС."""
    try:
        las = lasio.read(file_path)
        df = las.df()  # Конвертируем в pandas DataFrame
        df.reset_index(inplace=True)  # Глубина как колонка, а не индекс
        return df
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return None


def filter_anomalies(df: pd.DataFrame, curve: str, threshold: float) -> pd.DataFrame:
    """Удаляет аномальные значения (например, отрицательные сопротивления)."""
    return df[df[curve] < threshold]
