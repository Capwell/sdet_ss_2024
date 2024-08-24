import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .locators import RegistrationPageLocators as Locators


class RegistrationPage(BasePage):

    def set_first_name(self, input):
        self.set_input(Locators.LOCATOR_FIRST_NAME_FIELD, input)

    def set_last_name(self, input):
        self.set_input(Locators.LOCATOR_LAST_NAME_FIELD, input)

    def set_user_email(self, input):
        self.set_input(Locators.LOCATOR_USER_EMAIL_FIELD, input)

    def select_from_gender_radio(self, gender):
        """Возможные значения Male, Female, Other"""
        self.click(Locators.locator_gender_radio(self, gender))

    def set_user_number(self, input):
        self.set_input(Locators.LOCATOR_MOBILE_FIELD, input)

    def select_from_datepicker(self, dd_month_yyyy):
        """
            Ожидаем день, год в формате строки вида dd Month,yyyy
            Месяц, как английское название с заглавной.
            Например, "12 March,1977"
        """
        dd, month, yyyy = re.split(",| ", dd_month_yyyy)
        self.click(Locators.LOCATOR_BIRTH_DATEPICKER)
        self.set_input(Locators.LOCATOR_YEAR_BIRTH_DATEPICKER, yyyy)
        Select(self.driver.find_element(
            *Locators.LOCATOR_MONTH_BIRTH_DATEPICKER)
            ).select_by_visible_text(month)
        self.click(Locators.locator_day_birth_datapicker(self, dd))

    def set_upload_picture(self, file_path):
        self.set_input(Locators.LOCATOR_PICTURE_UPLOAD_FIELD, str(file_path))

    def set_subjects(self, input):
        """
            Список предметов с заглавной.
            Пример: ["Chemistry", "Social Studies"]
        """
        element = self.find_element(Locators.LOCATOR_SUBJECTS_FIELD)
        for subject in input:
            element.send_keys(subject)
            element.send_keys(Keys.ENTER)

    def select_from_dropdown(self, locator, value):
        self.click(locator)
        self.click(Locators.locator_select_from_dropdown(self, value))

    def set_current_adress(self, input):
        self.set_input(Locators.LOCATOR_CURRENT_ADDRES_FIELD, input)

    def set_state(self, input):
        self.select_from_dropdown(Locators.LOCATOR_STATE_DROPDOWN_FIELD, input)

    def set_city(self, input):
        self.select_from_dropdown(Locators.LOCATOR_CITY_DROPDOWN_FIELD, input)

    def push_submit_button(self):
        self.click(Locators.LOCATOR_SUBMIT_BUTTON)

    def get_modal_window_text(self):
        return self.get_text(Locators.LOCATOR_MODAL_WINDOW)

    def get_table_data(self):
        return self.get_text(Locators.LOCATOR_TABLE)

    def fill_registration_form(
            self,
            first_name,
            last_name,
            user_email,
            gender,
            user_number,
            birthday_date,
            subjects,
            file_path,
            current_adress,
            state,
            city,
            ):

        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_user_email(user_email)
        self.select_from_gender_radio(gender)
        self.set_user_number(user_number)
        self.select_from_datepicker(birthday_date)
        self.set_subjects(subjects)
        self.set_upload_picture(file_path)
        self.set_current_adress(current_adress)
        self.set_state(state)
        self.set_city(city)
