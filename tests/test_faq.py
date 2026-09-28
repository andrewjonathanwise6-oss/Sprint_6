import allure
import pytest

from data import FAQ_ANSWERS
from locators import MainPageLocators
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL


def normalize_text(text):
    return ' '.join(
        text
        .replace('\xa0', ' ')
        .replace('—', '-')
        .replace('–', '-')
        .split()
    )


class TestFAQ:

    @allure.title('Проверка текста ответа в FAQ')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_answer',
        [
            (MainPageLocators.FAQ_QUESTION_0, MainPageLocators.FAQ_ANSWER_0, FAQ_ANSWERS[0]),
            (MainPageLocators.FAQ_QUESTION_1, MainPageLocators.FAQ_ANSWER_1, FAQ_ANSWERS[1]),
            (MainPageLocators.FAQ_QUESTION_2, MainPageLocators.FAQ_ANSWER_2, FAQ_ANSWERS[2]),
            (MainPageLocators.FAQ_QUESTION_3, MainPageLocators.FAQ_ANSWER_3, FAQ_ANSWERS[3]),
            (MainPageLocators.FAQ_QUESTION_4, MainPageLocators.FAQ_ANSWER_4, FAQ_ANSWERS[4]),
            (MainPageLocators.FAQ_QUESTION_5, MainPageLocators.FAQ_ANSWER_5, FAQ_ANSWERS[5]),
            (MainPageLocators.FAQ_QUESTION_6, MainPageLocators.FAQ_ANSWER_6, FAQ_ANSWERS[6]),
            (MainPageLocators.FAQ_QUESTION_7, MainPageLocators.FAQ_ANSWER_7, FAQ_ANSWERS[7]),
        ]
    )
    def test_faq_answer_text_is_correct(self, driver, question_locator, answer_locator, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(MAIN_PAGE_URL)
        main_page.accept_cookies()

        main_page.click_faq_question(question_locator)
        actual_answer = main_page.get_faq_answer_text(answer_locator)

        assert normalize_text(actual_answer) == normalize_text(expected_answer)