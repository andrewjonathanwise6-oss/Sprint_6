import allure

from pages.base_page import BasePage
from locators import MainPageLocators, DzenPageLocators


class MainPage(BasePage):

    @allure.step('Принять cookies, если кнопка отображается')
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BUTTON)
        except Exception:
            pass

    @allure.step('Нажать на верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.click_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Нажать на нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_locator):
        self.click_element(question_locator)

    @allure.step('Получить текст ответа FAQ')
    def get_faq_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step('Закрыть попап установки Яндекс Браузера, если он появился')
    def close_yandex_browser_popup(self):
        try:
            self.click_element(DzenPageLocators.NO_THANKS_BUTTON)
        except Exception:
            pass