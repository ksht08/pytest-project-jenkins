import pytest
import allure
from allure_commons.types import AttachmentType

def test_pass_1():
    with allure.step("Строка в нижнем регистре"):
        assert "test".islower()

def test_pass_2():
    with allure.step("Проверяем длину списка"):
        assert len([1, 2, 3, 4]) == 4

def test_pass_3():
    with allure.step("Проверка словаря"):
        allure.attach("Словарь корректный", "log", AttachmentType.TEXT, ".log")
        assert {"a": 1}.get("a") == 1

def test_fail_1():
    with allure.step("Ошибка в числе"):
        assert 2 ** 3 == 16

def test_fail_2():
    with allure.step("Ошибка in"):
        assert "x" in "abcdef"
