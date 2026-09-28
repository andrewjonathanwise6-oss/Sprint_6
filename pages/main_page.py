import allure

from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Принять cookies, если кнопка отображается')
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_locator):
        self.click_element(question_locator)

    @allure.step('Получить текст ответа FAQ')
    def get_faq_answer_text(self, answer_locator):
        return self.get_text(answer_locator)