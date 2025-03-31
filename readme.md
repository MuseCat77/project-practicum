# активация venv
`source ./venv/bin/activate`
# установка зависимостей
`pip install -r requirements.txt`
# запуск тестирования (c активированным, который в папке playwright)
`pytest test.py`
# запуск locust (c активированным venv, который в папке locust)
`locust -f locust.py`
