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

def test_fail_4():
    with allure.step("Ошибка списка"):
        assert 3 in [1,2]

def test_fail_5():
    with allure.step("Ошибка словаря"):
        assert {"a":1}["a"] == 2
