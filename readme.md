# Проект SQLAlchemy + Flask 



## Запуск проекта
1) Устанавливаем виртуальное окружение
```
python -m venv venv

venv\Scripts\Activate
```
2) Устанавливаем зависимости
```
pip install -r requirements.txt
```
3) Запускаем приложение
```
$env:SQLALCHEMY_DATABASE_URI="sqlite:///project.db"
flask --app app.py run
```
