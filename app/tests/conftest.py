import pytest
from selenium import webdriver

from pathlib import Path
from ..settings import BASE_DIR
from ..pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def modal_window(request):
    link = "https://demoqa.com/automation-practice-form"
    driver = webdriver.Chrome()
    test_image = Path(BASE_DIR, "tests/fixtures", "test.jpg")

    data = {
        "first_name": "Иван",
        "last_name": "Иванов",
        "user_email": "test@test.ru",
        "gender": "Male",
        "user_number": 1234567890,
        "birthday_date": "12 March,1977",
        "subjects": ["English", "Chemistry", "Social Studies"],
        "file_path": test_image,
        "current_adress": "Произвольный адрес",
        "state": "NCR",
        "city": "Delhi",
    }

    request.cls.registration_page_link = link
    request.cls.test_form_data = data

    page = RegistrationPage(driver, link)
    page.open_link()
    page.fill_registration_form(**data)
    page.push_submit_button()
    request.cls.modal_window = page
    yield
    driver.quit()
