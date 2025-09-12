import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Сумма чисел равна 15"):
        assert sum([5, 5, 5]) == 15

def test_pass_2():
    with allure.step("Сравниваем множества"):
        assert {1, 2} | {3} == {1, 2, 3}

def test_pass_3():
    with allure.step("Булево условие выполняется"):
        allure.attach("Булево условие проверено", "log", AttachmentType.TEXT, ".log")
        assert 10 != 20

def test_fail_1():
    with allure.step("Неверное сравнение строк"):
        assert "python".startswith("java")

def test_fail_2():
    with allure.step("Ошибка в списке"):
        assert [1, 2, 3][-1] == 4
