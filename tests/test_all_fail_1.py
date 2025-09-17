import time
import allure

def test_fail_1():
    with allure.step("Неправильная математика"):
        time.sleep(1)
        assert 2 + 2 == 5

def test_fail_2():
    with allure.step("Строки не равны"):
        time.sleep(2)
        assert "hello" == "bye"
