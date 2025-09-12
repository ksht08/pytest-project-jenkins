import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Правильный тест"):
        assert 3*3 == 9

def test_pass_2():
    with allure.step("Строка в строке"):
        assert "a" in "apple"

def test_pass_3():
    with allure.step("Булевы значения"):
        allure.attach("Все хорошо", "log", AttachmentType.TEXT, ".log")
        assert True

def test_fail_1():
    with allure.step("Ошибочный тест"):
        assert 100 == 101

def test_fail_2():
    with allure.step("Ошибочная строка"):
        assert "pytest" == "unitest"
