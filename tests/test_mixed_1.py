import time
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Правильный тест"):
        assert 3*3 == 9

def test_pass_3():
    with allure.step("Булевы значения"):
        allure.attach("Все хорошо", "log", AttachmentType.TEXT, ".log")
        assert True

def test_fail_1():
    with allure.step("Ошибочный тест"):
        time.sleep(1)
        assert 100 == 101

