import allure

from pages.main_page import MainPage
from urls import MAIN_PAGE_URL


class TestLogo:

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(MAIN_PAGE_URL)
        main_page.accept_cookies()
        main_page.click_top_order_button()
        main_page.wait_until_url_contains('/order')

        main_page.click_scooter_logo()
        main_page.wait_until_url_to_be(MAIN_PAGE_URL)

        assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_opens_yandex_page_in_new_window(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(MAIN_PAGE_URL)
        main_page.accept_cookies()

        old_windows = main_page.get_window_handles()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window(old_windows)
        main_page.wait_until_url_is_not_blank()

        current_url = main_page.get_current_url()

        assert 'dzen.ru' in current_url or 'ya.ru' in current_url