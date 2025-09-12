import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Проверяем 1 + 1 == 2"):
        assert 1 + 1 == 2

def test_pass_2():
    with allure.step("Проверяем длину строки"):
        assert len("pytest") == 6

def test_pass_3():
    with allure.step("Все ок, true == true"):
        assert True is True

def test_pass_4():
    with allure.step("Сравнение чисел"):
        assert 10 > 5

def test_pass_5():
    with allure.step("Проверяем список"):
        allure.attach("Логи: список корректный", "log", AttachmentType.TEXT, ".log")
        assert [1, 2, 3][0] == 1
