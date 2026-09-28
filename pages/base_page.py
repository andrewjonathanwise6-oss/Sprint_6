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

    def get_current_url(self):
        return self.driver.current_url