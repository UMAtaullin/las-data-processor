# las-data-processor 
Парсер и анализатор LAS-файлов (ГИС данные)


## Возможности  
- Чтение LAS-файлов (`lasio`).  
- Фильтрация аномальных значений.  
- Построение графиков кривых ГИС (`matplotlib`).  


## Структура проекта:
las-data-processor/  
├── data/                  # Папка для тестовых LAS-файлов  
│   └── example.las  
├── las_parser/            # Основной код  
│   ├── __init__.py  
│   ├── parser.py          # Логика чтения LAS  
│   └── plotter.py         # Визуализация  
├── requirements.txt       # Зависимости  
└── README.md              # Описание проекта  

## Установка и запуск (результат появится в папке res):
```bash
git clone https://github.com/ваш-логин/las-data-processor.git
python3 -m venv .env
. .env/bin/activate
pip install -r requirements.txt
python main.py
```

## Что еще можно сделать:
1. Добавь обработку ошибок (например, если файл битый).  
2. Реализуй экспорт в CSV (`df.to_csv("output.csv")`).  
3. Сделай интерфейс командной строки (CLI) через `argparse`.  
4. Добавить машинное обучение для автоматической классификации литотипов😊    