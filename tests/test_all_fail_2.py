import pytest
import allure

def test_fail_1():
    with allure.step("Ошибка в математике"):
        assert 10 < 5

def test_fail_2():
    with allure.step("Ошибка в строке"):
        assert "PYTEST".islower()

def test_fail_3():
    with allure.step("Ошибка булева"):
        assert True is False