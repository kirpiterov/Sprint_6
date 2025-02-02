import allure
import pytest
from pages.main_page import MainPage
from datasets import TestDatasets


class TestAnswers:
    @allure.title('Тест ответов на вопросы')
    @pytest.mark.parametrize('question_number, expected_answer_text', TestDatasets.answers)
    def test_answers_for_questions(self,driver,question_number,expected_answer_text):
        main_page = MainPage(driver)
        main_page.click_cookie_confirm()
        main_page.wait_faq_panel_visibility()
        actual_text = main_page.click_to_question(question_number)

        assert actual_text == expected_answer_text