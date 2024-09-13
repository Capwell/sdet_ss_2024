# sdet_ss_2024

## Установка
Клонируйте репозиторий:

```git clone https://github.com/Capwell/sdet_ss_2024```

Перейдите в директорию проекта и установите зависимости

```poetry install```

При необходимости выбрерите локальную версию python (требуется установленный pyenv)

```pyenv local 3.10.14```

## Запуск тестов:
В директории проекта выполните команду для запуска

Все тесты

```poetry run pytest```

С подробным выводом в консоль

```poetry run pytest -vv```

Только smoke-тест

```poetry run pytest -s -v -m smoke```

Тесты из ТЗ

```poetry run pytest -s -v -m webtest```

С логированием в allure:

```poetry run pytest --alluredir=./allure-results```
