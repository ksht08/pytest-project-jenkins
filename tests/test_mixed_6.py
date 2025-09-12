import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Список равен самому себе"):
        assert [1, 2, 3] == [1, 2, 3]

def test_pass_2():
    with allure.step("Проверяем оператор in"):
        assert "t" in "pytest"

def test_pass_3():
    with allure.step("Числа совпадают"):
        allure.attach("Числа равны", "log", AttachmentType.TEXT, ".log")
        assert 42 == 42

def test_fail_1():
    with allure.step("Ошибка в сравнении чисел"):
        assert 100 < 50

def test_fail_2():
    with allure.step("Ошибка словаря"):
        assert {"x": 10}["x"] == 20
