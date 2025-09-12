import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Сумма чисел работает"):
        assert 7 + 8 == 15

def test_pass_2():
    with allure.step("Проверяем пустую строку"):
        assert "" == ""

def test_pass_3():
    with allure.step("True эквивалентен bool(1)"):
        allure.attach("Булево значение совпадает", "log", AttachmentType.TEXT, ".log")
        assert True == bool(1)

def test_fail_1():
    with allure.step("Неверная длина строки"):
        assert len("pytest") == 10

def test_fail_2():
    with allure.step("Неверное сравнение списков"):
        assert [1, 2] == [2, 1]
