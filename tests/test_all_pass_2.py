import time
import allure

def test_pass_1():
    time.sleep(1)
    with allure.step("Сравниваем строки"):
        assert "hi".upper() == "HI"

def test_pass_2():
    with allure.step("Сравниваем числа"):
        time.sleep(1)
        assert 5 * 2 == 10

def test_pass_3():
    with allure.step("Булево сравнение"):
        time.sleep(1)
        assert not False

