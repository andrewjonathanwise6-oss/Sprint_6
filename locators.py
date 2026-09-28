from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = By.XPATH, "//button[text()='да все привыкли']"

    FAQ_QUESTION_0 = By.ID, "accordion__heading-0"
    FAQ_QUESTION_1 = By.ID, "accordion__heading-1"
    FAQ_QUESTION_2 = By.ID, "accordion__heading-2"
    FAQ_QUESTION_3 = By.ID, "accordion__heading-3"
    FAQ_QUESTION_4 = By.ID, "accordion__heading-4"
    FAQ_QUESTION_5 = By.ID, "accordion__heading-5"
    FAQ_QUESTION_6 = By.ID, "accordion__heading-6"
    FAQ_QUESTION_7 = By.ID, "accordion__heading-7"

    FAQ_ANSWER_0 = By.ID, "accordion__panel-0"
    FAQ_ANSWER_1 = By.ID, "accordion__panel-1"
    FAQ_ANSWER_2 = By.ID, "accordion__panel-2"
    FAQ_ANSWER_3 = By.ID, "accordion__panel-3"
    FAQ_ANSWER_4 = By.ID, "accordion__panel-4"
    FAQ_ANSWER_5 = By.ID, "accordion__panel-5"
    FAQ_ANSWER_6 = By.ID, "accordion__panel-6"
    FAQ_ANSWER_7 = By.ID, "accordion__panel-7"