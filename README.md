# sdet_ss_2024

Клонируйте репозиторий:

Для запуска проекта нужно установить зависимости
poetry install
При необходимости выбрать локальную версию python (требуется установленный pyenv)
pyenv local 3.10.14

Для запуска тестов:
poetry run pytest

Для запуска тестов с логированием в allure:
poetry run pytest --alluredir=./allure-results