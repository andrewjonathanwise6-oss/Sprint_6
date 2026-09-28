from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def click_element(self, locator):
        self.find_clickable_element(locator).click()

    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_until_element_is_invisible(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def wait_until_url_contains(self, url_part):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(url_part)
        )

    def wait_until_url_to_be(self, url):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(url)
        )

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_new_window(self, old_windows):
        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(old_windows)
        )

        new_windows = [
            window for window in self.driver.window_handles
            if window not in old_windows
        ]

        self.driver.switch_to.window(new_windows[0])

    def get_current_url(self):
        return self.driver.current_url

    def wait_until_url_is_not_blank(self):
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.current_url not in ('about:blank', 'about:newtab')
        )

    def wait_until_url_contains_any(self, url_parts):
        WebDriverWait(self.driver, 20).until(
            lambda driver: any(url_part in driver.current_url for url_part in url_parts)
        )