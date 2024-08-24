from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # При поиске элементов на странице использовать
    # как минимум по одному селектору из перечисленных: css, xpath, id
    LOCATOR_FIRST_NAME_FIELD = (By.ID, "firstName")
    LOCATOR_LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    LOCATOR_USER_EMAIL_FIELD = (By.XPATH, "//*[@id='userEmail']")

    LOCATOR_MOBILE_FIELD = (By.XPATH, "//*[@id='userNumber']")
    LOCATOR_BIRTH_DATEPICKER = (By.XPATH, "//*[@id='dateOfBirthInput']")
    LOCATOR_YEAR_BIRTH_DATEPICKER = (
        By.XPATH, "//*[contains(@class, 'react-datepicker__year-select')]"
    )
    LOCATOR_MONTH_BIRTH_DATEPICKER = (
        By.CLASS_NAME, "react-datepicker__month-select"
    )
    # LICATOR_HOBBIES = (By.XPATH, "//*[@id='subjects-label']")
    LOCATOR_PICTURE_UPLOAD_FIELD = (By.XPATH, "//*[@id='uploadPicture']")
    LOCATOR_SUBJECTS_FIELD = (By.XPATH, "//*[@id='subjectsInput']")
    LOCATOR_PICTURE_FILEFIELD = (By.XPATH, "//*[@id='uploadPicture']")
    LOCATOR_CURRENT_ADDRES_FIELD = (By.XPATH, "//*[@id='currentAddress']")
    LOCATOR_STATE_DROPDOWN_FIELD = (By.XPATH, "//*[@id='state']")
    LOCATOR_CITY_DROPDOWN_FIELD = (By.XPATH, "//*[@id='city']")

    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//*[@id='submit']")

    LOCATOR_MODAL_WINDOW = (By.XPATH, "//*[@id='example-modal-sizes-title-lg']")
    LOCATOR_TABLE = (By.XPATH, "//*[contains(@class, 'table-responsive')]")

    def locator_gender_radio(self, gender):
        """Возможные значения Male, Female, Other"""
        gender_to_index = {
            "Male": 1,
            "Female": 2,
            "Other": 3,
        }
        return (By.XPATH, f"//label[@for='gender-radio-{gender_to_index[gender]}']")

    def locator_day_birth_datapicker(self, dd):
        """Ожидаем дату из 2х цифр."""
        return (By.XPATH, f"//*[contains(@class, 'react-datepicker__day') and text()='{dd}']")

    def locator_select_from_dropdown(self, value):
        return (By.XPATH, f"//*[text()='{value}']")
