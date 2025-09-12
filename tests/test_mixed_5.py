import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Обычная математика"):
        assert 50 / 10 == 5

def test_pass_2():
    with allure.step("Проверка строки"):
        assert "QA".lower() == "qa"

def test_pass_3():
    with allure.step("Проверка множества"):
        allure.attach("Множество совпало", "log", AttachmentType.TEXT, ".log")
        assert set([1, 2, 3]) == {3, 2, 1}

def test_fail_1():
    with allure.step("Неправильная математика"):
        assert 9 - 3 == 10

def test_fail_2():
    with allure.step("Строки не равны"):
        assert "abc" == "xyz"
