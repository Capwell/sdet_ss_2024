import allure
import pytest
import requests
from pathlib import PurePath


@pytest.mark.usefixtures("modal_window")
@allure.epic("Тестирование формы регистрации")
class TestRegistrationPage():
    @pytest.mark.smoke
    @allure.feature("smoke")
    @allure.story("Проверка статуса ответа эндпоинта")
    def test_link(self):
        response = requests.get(self.modal_window.link)
        with allure.step(f"Запрос к {self.registration_page_link} отправлен"):
            assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    @pytest.mark.webtest
    @allure.feature("webtest")
    @allure.story("Проверка содержимого текста модального окна")
    def test_registration_page_modal_window_text(self):
        """
            После нажатия кнопки submit
            появилось всплывающее окно с заголовком Thanks for submitting the form.
        """
        expected_content = "Thanks for submitting the form"
        with allure.step("Проверено содержимое текста модального окна"):
            assert self.modal_window.get_modal_window_text() == expected_content, "Заголовок отличается от отжидаемого"

    @pytest.mark.webtest
    @allure.feature("webtest")
    @allure.step("Проверка содержимого таблицы модального окна")
    def test_registration_page_modal_window_table_data(self):
        """
            После нажатия кнопки submit
            В таблице на окне отображаются введенные ранее значения.
        """
        expected_content = [
            "Label Values",
            f"Student Name {self.test_form_data['first_name']} {self.test_form_data['last_name']}",
            f"Student Email {self.test_form_data['user_email']}",
            f"Gender {self.test_form_data['gender']}",
            f"Mobile {self.test_form_data['user_number']}",
            f"Date of Birth {self.test_form_data['birthday_date']}",
            f"Subjects {', '.join(self.test_form_data['subjects'])}",
            "Hobbies",  # Нет в ТЗ. Метод не создан
            f"Picture {PurePath(self.test_form_data['file_path']).name}",
            f"Address {self.test_form_data['current_adress']}",
            f"State and City {self.test_form_data['state']} {self.test_form_data['city']}",
        ]
        with allure.step("Проверено содержимое таблицы модального окна"):
            assert self.modal_window.get_table_data().split("\n") == expected_content, (
                "Данные в таблице отличаются от ожидаемых"
            )
