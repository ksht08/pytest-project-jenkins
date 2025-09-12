import pytest
import allure

def test_pass_1():
    with allure.step("Сравниваем строки"):
        assert "hi".upper() == "HI"

def test_pass_2():
    with allure.step("Сравниваем числа"):
        assert 5 * 2 == 10

def test_pass_3():
    with allure.step("Булево сравнение"):
        assert not False

def test_pass_4():
    with allure.step("Проверяем in"):
        assert "py" in "pytest"

def test_pass_5():
    with allure.step("Множество"):
        assert {1,2,3} == {3,2,1}
