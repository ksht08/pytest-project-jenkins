import pytest
import allure

def test_fail_1():
    with allure.step("Неправильная математика"):
        assert 2 + 2 == 5

def test_fail_2():
    with allure.step("Строки не равны"):
        assert "hello" == "bye"

def test_fail_3():
    with allure.step("Булево сравнение"):
        assert False
