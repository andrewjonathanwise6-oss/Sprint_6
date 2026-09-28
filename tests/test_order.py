import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import MAIN_PAGE_URL


class TestOrder:

    @allure.title('Позитивный сценарий заказа самоката через верхнюю кнопку')
    @pytest.mark.parametrize('order_data', ORDER_DATA)
    def test_order_scooter_from_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_page(MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.fill_first_order_form(order_data)
        order_page.fill_second_order_form(order_data)
        order_page.submit_order()

        success_text = order_page.get_success_order_text()

        assert 'Заказ оформлен' in success_text

    @allure.title('Позитивный сценарий заказа самоката через нижнюю кнопку')
    def test_order_scooter_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_data = ORDER_DATA[0]

        main_page.open_page(MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page.fill_first_order_form(order_data)
        order_page.fill_second_order_form(order_data)
        order_page.submit_order()

        success_text = order_page.get_success_order_text()

        assert 'Заказ оформлен' in success_text