import lasio
import pandas as pd
from typing import Optional


def load_las(file_path: str) -> Optional[pd.DataFrame]:
    """Загружает LAS-файл и возвращает DataFrame с кривыми ГИС."""
    try:
        las = lasio.read(file_path)
        df = las.df()  # Конвертируем в pandas DataFrame
        df.reset_index(inplace=True)  # Глубина как колонка, а не индекс
        df.rename(columns={"DEPT.F": "DEPT"}, inplace=True)
        print("Загружены кривые:", df.columns.tolist())  # Логирование
        return df
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return None


def filter_anomalies(df: pd.DataFrame, curve: str, threshold: float) -> pd.DataFrame:
    """Фильтрует кривую, если она есть в данных."""
    if curve not in df.columns:
        available_curves = [
            col for col in df.columns if col.startswith(("RES", "RT", "ILD"))
        ]
        print(f"Кривая '{curve}' не найдена. Доступные аналоги: {available_curves}")
        return df
    return df[df[curve] < threshold]


def detect_curve_names(df: pd.DataFrame) -> dict:
    """Возвращает стандартные имена кривых, найденные в файле."""
    aliases = {
        "GR": ["GR", "GRC", "SGR"],  # Гамма-каротаж
        "RES": ["RES", "RESD", "RT", "ILD"],  # Сопротивление
        "NPHI": ["NPHI", "NPOR"],  # Нейтронная пористость (может отсутствовать)
        "DT": ["DT", "AC"],  # Акустика
    }
    found = {}
    for standard_name, variants in aliases.items():
        for variant in variants:
            if variant in df.columns:
                found[standard_name] = variant
                break
    return found
