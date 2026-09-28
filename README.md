\# Sprint\_6



Финальный проект 6 спринта: UI-автотесты для сервиса «Яндекс.Самокат».



\## Технологии



\- Python

\- pytest

\- Selenium

\- Firefox

\- Allure



\## Покрытая функциональность



\- Выпадающий список в разделе «Вопросы о важном».

\- Позитивный сценарий заказа самоката.

\- Проверка перехода по логотипу «Самокат».

\- Проверка перехода по логотипу Яндекса.



\## Запуск тестов





python -m pytest -v







\# Запуск тестов с Allure



\## python -m pytest --alluredir=allure\_results


#Генерация Allure-отчёта

##allure generate allure\_results -o allure\_report --clean



