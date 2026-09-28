import allure

from pages.base_page import BasePage
from locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    @allure.step('Заполнить первую форму заказа')
    def fill_first_order_form(self, order_data):
        self.set_text(OrderPageLocators.NAME_INPUT, order_data['name'])
        self.set_text(OrderPageLocators.SURNAME_INPUT, order_data['surname'])
        self.set_text(OrderPageLocators.ADDRESS_INPUT, order_data['address'])
        self.set_text(OrderPageLocators.METRO_INPUT, order_data['metro'])
        self.click_element(OrderPageLocators.metro_station_option(order_data['metro']))
        self.set_text(OrderPageLocators.PHONE_INPUT, order_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить вторую форму заказа')
    def fill_second_order_form(self, order_data):
        self.set_text(OrderPageLocators.DATE_INPUT, order_data['date'])
        self.find_element(OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)
        self.wait_until_element_is_invisible(OrderPageLocators.DATEPICKER)

        self.click_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.rent_period_option(order_data['rent_period']))
        self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        self.set_text(OrderPageLocators.COMMENT_INPUT, order_data['comment'])

    @allure.step('Подтвердить заказ')
    def submit_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Получить текст окна успешного заказа')
    def get_success_order_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_ORDER_MODAL)